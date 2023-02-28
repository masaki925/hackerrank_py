#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#


def largestRectangle(h):
    print(f"{h=}")
    res = 0
    stack = []

    # increasing stack
    # when got smaller num
    #   _h = pop
    #   max(res, (i -- k) * _h)
    for i, _h in enumerate(h):
        start = i
        while stack and _h < stack[-1][1]:
            j, hh = stack.pop()
            res = max(res, (i - j) * hh)
            start = j

        stack.append([start, _h])

    while stack:
        j, hh = stack.pop()
        res = max(res, (len(h) - j) * hh)

    return res


if __name__ == "__main__":
    fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

    with open("./tc1") as fp:
        while line := fp.readline():
            n = int(line.strip())

            line = fp.readline()
            h = list(map(int, line.rstrip().split()))

            result = largestRectangle(h)

            fptr.write(str(result) + "\n")

            fptr.close()
