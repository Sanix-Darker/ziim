# Just to import Ziim
from ziim.module import Ziim

try:
    # Your code here
    test = "test" + 12  # This will throws an error
except Exception as es:
    # Then call ziim here
    Ziim().go(es)
