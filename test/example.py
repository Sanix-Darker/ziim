# Just to import Zeus
from os import path as ospath
from sys import path as syspath
# moving the path outside of the current dir
syspath.insert(1, ospath.join(syspath[0], '..'))
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