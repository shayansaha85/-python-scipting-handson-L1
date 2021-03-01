import sys


def isWhiteLine(s):
    return s.isspace()


file = sys.argv[1]
f = open(file, 'r')
for x in f:
    if not isWhiteLine(x):
        print(str(x).strip())
f.close()
