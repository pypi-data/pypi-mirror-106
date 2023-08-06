from aural import segment
from aural import erb
from aural import feature
from aural import young
from aural.young import Band
from aural.feature import AttackDecayFeatures as ADF
from aural.feature import summary_stats

class Config:
    def __init__( self ):
        self.filter_pad_samples = 64
        self.global_km_window_seconds = 0.25
        self.local_km_window_seconds = 0.008
        self.filter_n = 100
        self.filter_min_hz = 50

    @property
    def filter_pad_samples( self ):
        '''The number samples used to absorb the gammatone filter's edge effects
'''
        return self.__filter_pad_samples

    @filter_pad_samples.setter
    def filter_pad_samples( self, i ):
        self.__filter_pad_samples = i

    @property
    def global_km_window_seconds( self ):
        '''The Kliewer-Mertins energy window duration (in seconds) for performing the call isolation.
'''
        return self.__global_km_window_seconds

    @global_km_window_seconds.setter
    def global_km_window_seconds( self, t ):
        self.__global_km_window_seconds = t

    @property
    def local_km_window_seconds( self ):
        '''The Kliewer-Mertins energy window duration (in seconds) for calculating the local attack/decay segments for each band in the filter-bank.
'''
        return self.__local_km_window_seconds

    @local_km_window_seconds.setter
    def local_km_window_seconds( self, t ):
        self.__local_km_window_seconds = t

    @property
    def filter_n( self ):
        '''The number of filter channels in the gammatone filterband
'''
        return self.__filter_n

    @filter_n.setter
    def filter_n( self, n ):
        self.__filter_n = n

    @property
    def filter_min_hz( self ):
        '''The starting frequency of the gammatone filterbank, in Hz
'''
        return self.__filter_min_hz

    @filter_min_hz.setter
    def filter_min_hz( self, f ):
        self.__filter_min_hz = f

class IsolationFailed( Exception ):
    def __init__( self ):
        pass

def extract( timeseries, fs, config ):
    '''This function will attempt isolate and extract a feature-set from a marine mammal vocalization, using techniques from literature reviewed as part of DFO contract FP967-21DATA3

    :param timeseries: A numpy array of raw timeseries data samples
    :param fs: Timeseries samplerate, in Hz
    :param config: An instance of meridian.Config tailored as needed
    :return: A tuple of features, or raises IsolationFailed if the vocalization could not be properly isolated.
'''

    isolated = young.isolate( timeseries, fs,
                              config.global_km_window_seconds,
                              config.filter_pad_samples )

    if not isolated.size: raise IsolationFailed

    # Center frequencies (in Hz) for filterbank
    FCs = erb.equally_spaced_erb( fmin = config.filter_min_hz, fs = fs,
                                  N = config.filter_n )
    # And also in ERB for features
    ERBs = list( map( erb.erb, FCs ))

    bands = young.filter( isolated, config.filter_pad_samples, fs, FCs )

    young.equalize_loudness( bands, FCs )

    features = young.attack_decay_features( bands, fs,
                                            config.local_km_window_seconds )

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

    duration = bands.shape[2] / fs
    return duration, spectro_temp

