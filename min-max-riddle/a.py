#!env python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    print(f"{arr=}")
    res = []

    for i in range(len(arr)):
        sub = []
        for j in range(len(arr) + 1):
            if j + i + 1 > len(arr):
                continue
            tmp = arr[j : j + i + 1]
            if tmp:
                sub.append(min(tmp))
        res.append(max(sub))

    return res


if __name__ == "__main__":
    fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

    with open("./in") as fp:
        while line := fp.readline():
            n = int(line)

            line = fp.readline()
            arr = list(map(int, line.rstrip().split()))

            res = riddle(arr)

            fptr.write(" ".join(map(str, res)))
            fptr.write("\n")

            fptr.close()
