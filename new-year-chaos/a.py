#!python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    res = 0

    for i in range(len(q) - 1, -1, -1):
        if q[i] != i + 1:
            if i - 1 >= 0 and q[i - 1] == i + 1:
                res += 1
                q[i - 1], q[i] = q[i], q[i - 1]
            elif i - 2 >= 0 and q[i - 2] == i + 1:
                res += 2
                q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
                q[i - 1], q[i] = q[i], q[i - 1]
            else:
                print("Too chaotic")
                return

    print(res)


if __name__ == "__main__":
    with open("./input") as fp:
        while True:
            line = fp.readline()
            if not line:
                break

            t = int(line.strip())

            for t_itr in range(t):
                line = fp.readline()
                n = int(line.strip())

                line = fp.readline()
                q = list(map(int, line.rstrip().split()))

                print(f"{q=}")
                minimumBribes(q)
