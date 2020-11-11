import argparse
# Just to import Ziim
from ziim.module import Ziim


if __name__ == "__main__":
    # Initialize the arguments
    prs = argparse.ArgumentParser()
    prs.add_argument('-c', '--command', help='The command you want to write', type=str)
    prs = prs.parse_args()

    # We execute the zm method
    Ziim().zm(str(prs.command))
