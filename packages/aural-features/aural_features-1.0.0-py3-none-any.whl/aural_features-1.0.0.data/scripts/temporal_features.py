#!python
import os
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as pp

from aural import segment
from aural import erb
from aural import feature
from aural import young
from aural.young import Band
from aural.feature import AttackDecayFeatures as ADF
from aural.feature import summary_stats

from collections import namedtuple
from argparse import ArgumentParser

parser = ArgumentParser( description="Calculate temporal features described by Victor Young's thesis from a group of wave files. For each (already isolated) detection wave file, calculate the global/local attack/decay feature statistics as well as the duration and synchronicity features." )

parser.add_argument( 'inputdir', help='Directory to scan for wave files' )
parser.add_argument( '-g','--global-km-window-seconds', type=float,
                     help='Global KM window width in seconds [default=0.25s]',
                     default=0.25,
                     metavar='sec' )
parser.add_argument( '-l','--local-km-window-seconds', type=float,
                     help='Local KM window width in seconds [default=0.008s]',
                     default=0.008,
                     metavar='sec' )

advanced = parser.add_argument_group( 'advanced' )
advanced.add_argument( '--pad-samples', metavar='N', type=int,
                       help='Use N samples of padding to absorb filtering edge effects.  These are thrown away after the filtering stage. [default=64]',
                       default=64 )

debug = parser.add_argument_group( 'debugging' )
debug.add_argument( '--show-plots', action='store_true',
                     help='Show a few plots of bands N=1,10,50, and global' )
debug.add_argument( '-V', '--verbose', action='store_true',
                    help='Make some noise during processing' )

args = parser.parse_args()



# First isolate the calls using the global KM algorithm
call = namedtuple( 'call', [ 'name', 'fs', 'padded_timeseries' ] )
pad = args.pad_samples
isolated_call_data = []
wavefiles = [ i for i in os.listdir( args.inputdir ) if i.endswith( '.wav' ) ]
for wavefile in wavefiles:
    fs,y = scipy.io.wavfile.read( os.path.join( args.inputdir, wavefile ))

    # Isolate, and add padding to the isolated call, which will be accounted
    # for in the filtering stage
    isolated = young.isolate( y, fs, args.global_km_window_seconds, pad )
    if not isolated.size:
        print( 'Skipping {}, cannot isolate attack/decay'.format( wavefile ))
        continue

    isolated_call_data.append( call( wavefile, fs, isolated ))

# Next process each isolated call
filter_n = 100
results = []
show_bands = [ 1, 10, 50 ] if args.show_plots else []
for call in isolated_call_data:

    # Center frequencies (in Hz) for filterbank
    FCs = erb.equally_spaced_erb( fmin = 50.0, fs = call.fs, N = filter_n )
    # And also in ERB for features
    ERBs = list( map( erb.erb, FCs ))

    bands = young.filter( call.padded_timeseries, pad, call.fs, FCs )

    young.equalize_loudness( bands, FCs )

    features = young.attack_decay_features( bands, call.fs,
                                            args.local_km_window_seconds )

    for i in show_bands:
        band = bands[i]
        pp.subplot( 211 )
        pp.title( "{} band {:10.2f} Hz".format( call.name, FCs[ i ] ) )
        pp.plot( band[ Band.timeseries ] )
        pp.subplot( 212 )
        pp.plot( band[ Band.envelope ] )
        scale = np.max( band[ Band.envelope ] ) / 3

        N = int( call.fs * args.local_km_window_seconds )
        Fattack, Fdecay = segment.kliewer_mertins( band[ Band.squared ], N )
        peak = np.argmax( band[ Band.envelope ][1:-1] ) + 1
        attack_beg = np.argmax( Fattack[:peak] )
        decay_offset = peak+1
        decay_end = np.argmax( Fdecay[decay_offset:] ) + decay_offset

        Fattack /= np.max( Fattack ) / scale
        Fdecay /= np.max( Fdecay ) / scale
        pp.plot( Fattack, color='green' )
        pp.plot( Fdecay, color='red' )
        pp.axvline( attack_beg, color='green', linestyle='--' )
        pp.axvline( peak, color='black', linestyle='--', alpha=0.5 )
        pp.axvline( decay_end, color='red', linestyle='--' )
        pp.show()


    sbsync = young.subband_synchronicity( bands )

    # Calculate summary statistics
    spectro_temp = feature.spectro_temporal(
        local_SBAT = summary_stats( features[ :,ADF.localSBAT ], ERBs ),
        local_SBAS = summary_stats( features[ :,ADF.localSBAS ], ERBs ),
        local_SBDT = summary_stats( features[ :,ADF.localSBDT ], ERBs ),
        local_SBDS = summary_stats( features[ :,ADF.localSBDS ], ERBs ),
        global_SBAT = summary_stats( features[ :,ADF.globalSBAT ], ERBs ),
        global_SBAS = summary_stats( features[ :,ADF.globalSBAS ], ERBs ),
        global_SBDT = summary_stats( features[ :,ADF.globalSBDT ], ERBs ),
        global_SBDS = summary_stats( features[ :,ADF.globalSBDS ], ERBs ),
        subband_synchronicity = summary_stats( sbsync, ERBs ),
    )

    duration = bands.shape[2] / call.fs
    results.append( ( call.name, duration, spectro_temp ) )


def print_stats( s ):
    print( f'    min  = {s.min:.6f}' )
    print( f'    fmin = {s.fmin:.6f}' )
    print( f'    mean = {s.mean:.6f}' )
    print( f'    max  = {s.max:.6f}' )
    print( f'    fmax = {s.fmax:.6f}' )

if args.verbose:
    for name,duration,spectro_temporal in results:
        print( name )
        for key, val in spectro_temporal._asdict().items():
            print( f'  {key}' )
            print_stats( val )

        print( '  duration' )
        print( f'    {duration:.4f}' )

