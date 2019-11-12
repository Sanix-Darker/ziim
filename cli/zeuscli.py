# Just to import Zeus
from os import system, path as ospath
from sys import exit, path as syspath
import sys
# moving the path outside of the current dir
syspath.insert(1, ospath.join(syspath[0], '..'))
import src.Zeus as Zeus
# Just to import Zeus

from subprocess import Popen, PIPE, STDOUT


def remove2points(output):
    for lign in str(output).split("\n"):
        if "Err" in lign or "Exception" in lign:
            return lign.split(":")[1]
    return ""

argg = sys.argv
del argg[0]
command = ' '.join(argg)

try:
    # Your code here
    # system(command+" > zcli_output.txt")
    proc = Popen(command.split(" "), stdout=PIPE, stderr=STDOUT)
    output = proc.communicate()[0].decode('utf-8')
    print(output)
    error = remove2points(output)
    if len(error)>1:
        Zeus.Zeus().go(error)
except KeyboardInterrupt:
    print("Thank you using zeus-cli")
    exit()
