#!env python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    print(f"{arr=}")
    if max(arr) <= 0:
        return 0

    # one, two = 0, 0

    # for i in range(len(arr)):
    #     print(f"{i=}, {one=}, {two=}")
    #     tmp = max(one, two, arr[i], one + arr[i])
    #     one = two
    #     two = tmp
    # return two

    arr += [0, 0]
    res = [0] * len(arr)

    for i in range(len(arr) - 3, -1, -1):
        print(f"{i=}, {arr=}")
        res[i] = max(arr[i], res[i + 1], arr[i] + res[i + 2])

    return res[0]


if __name__ == "__main__":
    with open("./in2") as fp:
        while line := fp.readline():
            fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

            n = int(line)

            line = fp.readline()
            arr = list(map(int, line.rstrip().split()))

            res = maxSubsetSum(arr)

            fptr.write(str(res) + "\n")

            fptr.close()
