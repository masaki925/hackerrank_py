#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

from collections import Counter


def pairs(k, arr):
    print(f"{k=}, {arr=}")
    res = 0

    cnt = Counter(arr)
    print(f"{cnt=}")

    for key in cnt.keys():
        diff = key + k
        if diff in cnt:
            res += cnt[diff]

    return res


if __name__ == "__main__":
    with open("./in0") as fp:
        while line := fp.readline():
            fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

            first_multiple_input = line.rstrip().split()

            n = int(first_multiple_input[0])

            k = int(first_multiple_input[1])

            line = fp.readline()
            arr = list(map(int, line.rstrip().split()))

            result = pairs(k, arr)

            fptr.write(str(result) + "\n")

            fptr.close()
