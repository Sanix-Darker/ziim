# import argparse
# # Just to import Ziim
# from ziim.module import Ziim
#
#
# if __name__ == "__main__":
#     # Initialize the arguments
#     prs = argparse.ArgumentParser()
#     prs.add_argument('-c', '--command', help='The command you want to write', type=str)
#     prs = prs.parse_args()
#
#     # We execute the zm method
#     Ziim().zm(str(prs.command))
from sys import argv
from ziim.module import Ziim

HELP_MSG = """Welcome to Ziim !
Usage: ziim [-h] [COMMAND]

optional arguments:
  -h, --help            show this help message and exit
  COMMAND,              The command you want to write
- - - - - - - - - -
By s@n1x-d4rk3r (github.com/sanix-darker/ziim)"""


if __name__ == "__main__":
    # we delete the first argument
    del argv[0]
    if argv[0] == "-h" or argv[0] == "--help":
        print(HELP_MSG)
    else:
        # We execute the zm method
        Ziim().zm(' '.join(argv))
