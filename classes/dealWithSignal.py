import signal
import sys
 
def handler(signum, frame):
    sys.exit(1)
 
 
signal.signal(signal.SIGINT, handler)
