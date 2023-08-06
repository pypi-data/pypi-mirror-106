import enum
import itertools
from collections import namedtuple

class AttackDecayFeatures( enum.IntEnum ):
    '''Convenience enum for interim features used to calculate the final
    summary statistics.  {global/local, sub-band attack/decay, time/slope}
    Acronyms borrowed from Young/Hines Perception-based automatic classification
    of impulsive-source active sonar echos [2007].
    '''
    globalSBAT = 0
    globalSBAS = 1
    globalSBDT = 2
    globalSBDS = 3
    localSBAT = 4
    localSBAS = 5
    localSBDT = 6
    localSBDS = 7

def time_and_slope( data, ibeg, iend, fs ):
    '''Helper function to pluck the time and slope from a curve
    '''
    rise = data[iend] - data[ibeg]
    run = (iend-ibeg)/fs
    slope = rise / run
    return run, slope

# Named type for summary stats
stats = namedtuple( 'stats', [ 'min', 'fmin', 'mean', 'max', 'fmax' ] )

def summary_stats( channel_features, ERBs ):
    '''Calculate summary statistics across channels for a given feature vector
'''
    return stats( min = channel_features.min(),
                  fmin = ERBs[ channel_features.argmin() ],
                  mean = channel_features.mean(),
                  max = channel_features.max(),
                  fmax = ERBs[ channel_features.argmax() ] )

# Generate names for all 2x4 combinations of attack/decay features
_prefix = [ 'local', 'global' ]
_feature = [ 'SBAT', 'SBAS', 'SBDT', 'SBDS' ]
_spectro_temporal = [ "_".join( itr ) for itr in itertools.product( _prefix, _feature ) ]

# Also subband synchronicity
_spectro_temporal.append( 'subband_synchronicity' )

# Export a convenient named data type for spectro_temporal features
spectro_temporal = namedtuple( "spectro_temporal", _spectro_temporal )

