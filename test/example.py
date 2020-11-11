# Just to import Ziim
from os import path as ospath
from sys import path as syspath
# moving the path outside of the current dir
syspath.insert(1, ospath.join(syspath[0], '..'))
import src.Ziim as Ziim
# Just to import Ziim

try:
    # Your code here
    test = "test"+12 # This will throws an error
except Exception as es:
    print(es)
    # Then call ziim here
    Ziim.Ziim().go(es)
    # That's all !