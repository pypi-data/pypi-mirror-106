import numpy as np

def erb( f ):
    '''Return the frequency f (Hz) in ERB units.
    '''
    # Victor Young's thesis eqn 6.6
    return 24.4 * np.log10( 0.00437 * f + 1.0 )

def equally_spaced_erb( fmin, fs, N ):
    '''Return a list N of frequencies (in Hz) which have been calculated to be
    equally spaced on the ERB scale.
    '''
    # Victor Young's thesis eqn 6.7
    i = np.arange( N ) + 1
    arg = i * ( np.log( fmin + 228.8 ) - np.log( fs/2.0 + 228.8 )) / N
    cf = np.exp( arg ) * ( fs/2.0 + 228.8 ) - 228.8
    return np.flip( cf )
