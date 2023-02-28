#!env python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    print(f"{a=}, {b=}, {c=}")
    res = 0
    a, b, c = sorted(list(set(a))), sorted(list(set(b))), sorted(list(set(c)))
    print(f"{a=}, {b=}, {c=}")

    for i in range(len(b)):
        ai = 0
        while ai < len(a) and a[ai] <= b[i]:
            ai += 1
        ci = 0
        while ci < len(c) and c[ci] <= b[i]:
            ci += 1
        res += ai * ci

    return res


if __name__ == "__main__":
    fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

    with open("./in") as fp:
        while line := fp.readline():
            lenaLenbLenc = line.split()

            lena = int(lenaLenbLenc[0])

            lenb = int(lenaLenbLenc[1])

            lenc = int(lenaLenbLenc[2])

            line = fp.readline()
            arra = list(map(int, line.rstrip().split()))

            line = fp.readline()
            arrb = list(map(int, line.rstrip().split()))

            line = fp.readline()
            arrc = list(map(int, line.rstrip().split()))

            ans = triplets(arra, arrb, arrc)

            fptr.write(str(ans) + "\n")

            fptr.close()
