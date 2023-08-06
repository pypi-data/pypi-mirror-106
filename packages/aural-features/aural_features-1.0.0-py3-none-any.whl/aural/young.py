import enum
import math
import numpy as np
import scipy
import scipy.signal
import itertools

from aural.feature import AttackDecayFeatures as ADF
from aural.feature import time_and_slope
from aural import segment
from aural import iso226
from aural import weight
from aural import erb

class Band( enum.IntEnum ):
    '''Convenience enum to address columns by name
    '''
    timeseries = 0
    squared = 1
    envelope = 2

def isolate( y, fs, global_km_window_seconds, pad ):
    '''This function applies the 'modified' Kliewer-Mertins algorithm to isolate the beginning and end of a call as described in Young 6.3
    :param y: Raw timeseries vector of a detection event
    :param fs: Timeseries sample-rate in Hz
    :param global_km_window_seconds: The global KM window size in seconds
    :param pad: The number extra samples to pad the isolated call with. This padding is later discarded after applying the filters.

    :return: An isolated timeseries vector which is a subset of the vector y, or an empty array if the attack/decay/peak detection is not successful.
'''

    # Normalize so that max(abs(y)) == 32768
    # This is somewhat arbitrary, but the original Young thesis does this to
    # assign "temporary" physical values where 1 == 1uPa, 2 == 2uPa while
    # adjusting for loudness.  There may be some assumptions built into their
    # C and alpha values, so we'll mimic that here.
    y = np.asarray( y, 'float32' )
    y /= max( abs( y )) / (2**15)

    N=int( fs * global_km_window_seconds )
    Fattack, Fdecay = segment.kliewer_mertins( np.square( y ), N )
    envelope = abs( scipy.signal.hilbert( y ))

    # Search only within x[pad:-pad] so that we have extra padding for filter
    # edge effects.  This keeps the math simple, and is a safe assumption
    # as the (implied) coarse detector will center the detected events.
    attack_beg = np.argmax( Fattack[pad:-pad] ) + pad
    peak = np.argmax( envelope[pad:-pad] ) + pad
    decay_end = np.argmax( Fdecay[pad:-pad] ) + pad

    if not attack_beg < peak or not peak < decay_end:
        return np.array([])

    return y[ attack_beg-pad:decay_end+pad ]

def filter( padded_timeseries, pad, fs, FCs ):
    '''This function pre-calculates a matrix of filter-bank vectors described in the enum Band.  For each center-frequency in FCs, a gammatone filter is applied to the padded_timeseries.  This function also calculates squared and hilbert-transformed vectors for convenience.  Vectors are then trimmed by pad elements on both ends to discard filtering edge effects.

    :param padded_timeseries: A vector of raw timeseries values to be filtered
    :param pad: How many pad samples are to be removed after filtering
    :param fs: input samplerate in Hz
    :param FCs: 1d numpy array of center frequencies in Hz.
    :return: numpy matrix of dimension [n_filter, 3, len].
'''
    filter_n = FCs.size
    actual_length = padded_timeseries.size - 2*pad
    bands = np.empty( ( filter_n, len( Band ), actual_length ),
                      dtype='float32' )

    # Filter into sub-bands
    for i,(band,f) in enumerate( zip( bands, FCs )):
        # Filter & C-weight, then calculate envelope and energy curves
        # Here we filter the entire padded waveform, but only use the
        # region inside the pads in subsequent steps to ignore edge effects
        b,a = scipy.signal.gammatone( freq = f, ftype='iir', fs = fs )
        filtered = weight.C( f ) * \
                   scipy.signal.lfilter( b, a, padded_timeseries )

        band[ Band.envelope ] = abs( scipy.signal.hilbert( filtered ))[pad:-pad]

        band[ Band.timeseries ] = filtered[pad:-pad]

        band[ Band.squared ] = np.square( band[ Band.timeseries ] )

    return bands

def equalize_loudness( bands, FCs ):
    '''This function attempts to scale the timeseries data stored in the bands
matrix by calculating the scaling factor gamma described in Young's thesis 6.4. Scaling is done in-place, and this returns nothing.

    :param bands: A numpy matrix of dimensions [ n_filter, 3, len ].  n_filter
    is the number of filters in the filterbank.  The second dimension describes
    each of the precalculated vectors described in Bands enum.  The len
    dimension describes the length of those vectors.

    :param FCs: A numpy array describing the bands center frequencies in Hz,
    of length n_filter.

    :return:
'''
    # Calculate frequencies in ERB
    ERBs = list( map( erb.erb, FCs ))

    # Calculate 7-sone equal loudness scaling factor, gamma
    Ethresh = iso226.maf( FCs )
    # iso226 is in units of dB(SPL) re 20upA, go back to RMS uPa
    ref = 20
    Ethresh = np.power( 10, Ethresh / 20 ) * ref
    # Scale for propagation in ear
    Ethresh = np.multiply( Ethresh, weight.C( FCs ))

    # Get RMS uPa of each band, making the Estim basilar curve
    Estim = np.sqrt( bands[ :, Band.squared ].mean( axis=1 ))

    # Non-linear compression, and calculate correction factor
    C = 0.0702
    alpha = 0.2159
    Nprime = C * ( np.power( Estim, alpha ) - np.power( Ethresh, alpha ))
    area = scipy.integrate.trapezoid( y=Nprime.clip( min = 0.0 ), x=ERBs )
    gamma =  ( 7.0 / area )**2

    # Scale, taking care to scale the squared data twice
    bands *= gamma
    bands[ :, Band.squared ] *= gamma

def attack_decay_features( bands, fs, local_km_window_seconds ):
    '''For each band in the filterbank, this function calculates the eight attack/decay features described by Young 7.2 and 7.3.  Those are the combinations of global/local subband attack/decay time/slope.

    :param bands: A numpy matrix of [n_filter, Bands, len]
    :param fs: Input samplerate in Hz.
    :param local_km_window_seconds: The local KM window size in seconds
    :return: A numpy feature matrix of dimensions [ n_filter, AttackDecayFeatures]
'''

    n_filter = bands.shape[0]
    # Extract the 8 attack/decay features for each band
    features = np.empty( ( n_filter, len( ADF ) ) )
    for i,(band,band_feature) in enumerate( zip( bands, features )):
        # Calculate local attack begin and decay end.  This is constrained
        # so that peak is in the range [1:-1] and attack max must come before
        # the peak, and decay max must come after the peak.
        N = int( fs * local_km_window_seconds )
        Fattack, Fdecay = segment.kliewer_mertins( band[ Band.squared ], N )
        peak = np.argmax( band[ Band.envelope ][1:-1] ) + 1
        attack_beg = np.argmax( Fattack[:peak] )
        decay_offset = peak+1
        decay_end = np.argmax( Fdecay[decay_offset:] ) + decay_offset

        # Collect global/local attack/decay time/slope features for summary
        # statistics later
        t,slope = time_and_slope( band[ Band.envelope ], attack_beg, peak, fs )
        band_feature[ ADF.localSBAT ] = t
        band_feature[ ADF.localSBAS ] = slope

        t,slope = time_and_slope( band[ Band.envelope ], peak, decay_end, fs )
        band_feature[ ADF.localSBDT ] = t
        band_feature[ ADF.localSBDS ] = slope

        global_beg = 0
        global_end = band[ Band.timeseries ].size-1

        t,slope = time_and_slope( band[ Band.envelope ], global_beg, peak, fs )
        band_feature[ ADF.globalSBAT ] = t
        band_feature[ ADF.globalSBAS ] = slope

        t,slope = time_and_slope( band[ Band.envelope ], peak, global_end, fs )
        band_feature[ ADF.globalSBDT ] = t
        band_feature[ ADF.globalSBDS ] = slope

    return features

def subband_synchronicity( bands ):
    '''This function calculates the mean subband synchronicity vector from the given bands
    :param bands: A numpy vector of [ n_filter, Bands, len ]
    :returns: A 1d numpy array of n_filter correlation coefficient means
'''
    # Pre-calculate some common factors used to produce the correlation matrix
    envelopes = bands[ :, Band.envelope, : ]
    envelopes_sum = envelopes.sum( axis=1 )
    envelopes_sum_squares = np.square( envelopes ).sum( axis=1 )
    Nsamp = bands.shape[ 2 ]
    filter_n = bands.shape[ 0 ]

    corr = np.empty( ( filter_n, filter_n ) )
    for row,col in itertools.product( range(filter_n), range(filter_n) ):
        # Victor Young eqn 7.4 broken down into (A-B)/(sqrt(C)*sqrt(D))
        A = Nsamp * np.dot( envelopes[row], envelopes[col] )
        B = envelopes_sum[row] * envelopes_sum[col]

        C = Nsamp * envelopes_sum_squares[row] - np.square( envelopes_sum[row] )
        D = Nsamp * envelopes_sum_squares[col] - np.square( envelopes_sum[col] )

        corr[row,col] = (A-B) / ( math.sqrt( C ) * math.sqrt( D ))

    # calculate row-means of MxM matrix (M=filter_n), which is then used to
    # pluck summary statistics
    corr = corr.mean( axis = 1 )
    return corr

