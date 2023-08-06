#!python
import scipy.io.wavfile
from collections import namedtuple
from argparse import ArgumentParser
import pathlib

parser = ArgumentParser( description='Clip detections from MobySound recordings, using the .log formatted annotations of individual vocalizations.  Writes the output files to the current directory.' )
parser.add_argument( 'wavefile',
                     help='Name of wavefile, with an implied .log file',
                     metavar='file' )
parser.add_argument( '-s', '--context-seconds', type=float, default=1.0,
                     metavar='sec',
                     help='Seconds of context noise before and after detection [default=1.0s]' )
args = parser.parse_args()

myrange = namedtuple( "myrange", [ "start", "stop" ] )

times = []
logfilename = pathlib.Path( args.wavefile ).with_suffix( '.log' )
with open( logfilename, 'r', encoding='ascii' ) as log:
    for line in log:
        tmp = [ float( i ) for i in line.split() ]
        # Just want the first two columns, start/end time
        times.append( myrange( *tmp[:2] ))

fs,y = scipy.io.wavfile.read( args.wavefile )

for i,time in enumerate( times ):
    samples = myrange( int( (time.start - args.context_seconds)*fs ),
                       int( (time.stop + args.context_seconds)*fs ) )
    snip = y[ samples.start : samples.stop ]

    prefix = "{:03d}_".format( i )
    outname = prefix + pathlib.Path( args.wavefile ).name

    scipy.io.wavfile.write( outname, fs, snip )

