from sys import argv
from ziim.module import Ziim

if __name__ == "__main__":
    # we delete the first argument
    del argv[0]
    # We execute the zm method
    Ziim().zm(' '.join(argv))
