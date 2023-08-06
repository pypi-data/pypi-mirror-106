import numpy as np

def kliewer_mertins( squared_data, N ):
    '''Perform 'modified' KM algorithm as described by Young.

    :param squared_data: energy timeseries data
    :param N: window size in samples
    :return: tuple of (Fattack, Fdecay) curves
'''

    # Pad the array with an extra sample to ensure the windows are correctly
    # aligned
    yy = np.pad( squared_data, pad_width=1, mode='edge' )

    kernel = np.ones( N ) / N

    left = np.convolve( yy[:-N-1], kernel )
    right = np.convolve( yy[N+1:], kernel )

    Fattack = np.log( right / left ) * right
    Fdecay = np.log( left / right ) * left

    return Fattack, Fdecay


