def C( cf ):
    '''C-weight for a given center-frequency in Hz.
    '''
    return 1.007 * 12200**2 * cf**2 / ( cf**2 + 20.6**2 ) / ( cf**2 + 12200**2 )
