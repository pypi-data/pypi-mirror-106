#!python
import numpy as np
import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as pp

from aural import segment

from argparse import ArgumentParser

parser = ArgumentParser( description='Process and segment a file using modified KM' )

parser.add_argument( 'input', help='Wave file to process', metavar='wavfile' )

parser.add_argument( '-f', '--filter', type=int,
                     help='Optionally apply a low-pass at the specified cutoff frequency in Hz',
                     metavar='cutoff-hz' )

parser.add_argument( '-g', '--global-km-window-seconds', type=float,
                     help='Global KM window size in seconds [default=0.25s]',
                     default=0.25,
                     metavar='sec' )

parser.add_argument( '-b', '--binder-threshold', type=float,
                     help='Binder threshold [default=0.02]', default=0.02,
                     metavar='threshold' )

args = parser.parse_args()


fs,y = scipy.io.wavfile.read( args.input )

# Normalize so that max(abs) == 1
y = np.asarray( y, 'float32' )
y /= max( abs( y ))
time = np.arange( y.size ) / fs

# Plot the unfiltered timeseries
ax1 = pp.subplot( 311 )
ax1.margins( x=0 )
ax1.plot( time, y )
ax1.title.set_text( 'Timeseries' )

if args.filter:
    nyquist = fs/2
    b,a = scipy.signal.butter( 3, args.filter / nyquist )
    y = scipy.signal.filtfilt( b, a, y )

f,t,spec = scipy.signal.spectrogram( y, fs,
                                     noverlap=0.5, nfft=1024,
                                     mode='magnitude' )
ax2 = pp.subplot( 312 )
ax2.pcolormesh( t,f,spec,shading='auto' )
ax2.title.set_text( "Spectrogram" )
pp.ylim( top=400 )

z = scipy.signal.hilbert( y )
envelope = abs( z )

max_envelope_time = envelope.argmax()/fs
# Ignore edge effects of filter, if used
if args.filter: max_envelope_time = envelope[30:-30].argmax()/fs

Fattack, Fdecay = segment.kliewer_mertins( y**2, N=int(fs*args.global_km_window_seconds ))
max_attack_time = Fattack.argmax()/fs
max_decay_time = Fdecay.argmax()/fs


# Low pass filter for the graph
smoothed_envelope = np.convolve( envelope, np.ones( 64 ) / 64, mode='same' )
ax3 = pp.subplot( 313 )
ax3.margins( x = 0 )
ax3.plot( time, smoothed_envelope, label='Envelope, smoothed' )
ax3.plot( time, Fattack, label='KM Attack fn' )
ax3.plot( time, Fdecay, label='KM Decay fn' )
ax3.plot( time, Fattack > args.binder_threshold, label='Binder threshold' )
ax3.plot( time, Fdecay > args.binder_threshold, label='Binder threshold' )
ax1.axvline( max_attack_time, color='black', linestyle='--' )
ax1.axvline( max_decay_time, color='black', linestyle='--' )
ax2.axvline( max_attack_time, color='white', linestyle='--' )
ax2.axvline( max_decay_time, color='white', linestyle='--' )
ax3.axvline( max_envelope_time, color='black', alpha=0.75, linestyle=':' )
ax3.axvline( max_attack_time, color='black', linestyle='--' )
ax3.axvline( max_decay_time, color='black', linestyle='--' )
ax3.title.set_text( "Segmenting" )

ax3.legend()

pp.show()

