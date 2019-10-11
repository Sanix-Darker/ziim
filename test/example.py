# Just to import Zeus
import os,sys
# moving the path outside of the current dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import src.Zeus as Zeus
# Just to import Zeus

try:
    # Your code here
    test = "test"+12 # This will throws an error
except Exception as es:
    print(es)
    # Then call zeus here
    Zeus.Zeus().go(es)
    # That's all !
