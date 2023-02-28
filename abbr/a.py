#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def abbreviation(a, b):
    print(f"{a=},\n{b=}")

    # 1. exactly match
    # 2. match if do upper()
    # 3. delete and if backtrack(l+1, r)
    # 4. False

    dp = [[False] * (len(b) + 1) for x in range(len(a) + 1)]
    dp[len(a)][len(b)] = True

    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b), -1, -1):
            print(f"{i=}, {j=}")
            if j + 1 < len(b) and a[i].upper() == b[j] and dp[i + 1][j + 1]:
                dp[i][j] = True
            if j != len(b) and a[i].lower() and dp[i + 1][j]:
                dp[i][j] = True

            for ii in range(len(a) + 1):
                print(dp[ii])

    return "YES" if dp[0][0] else "NO"

    # dp[0][0] = True

    # for i in range(len(a)):
    #     for j in range(len(b) + 1):
    #         print(f"{i=}, {j=}")
    #         if j < len(b) and a[i].upper() == b[j] and dp[i][j]:
    #             dp[i + 1][j + 1] = True
    #         if a[i].islower():
    #             dp[i + 1][j] = True

    #         for ii in range(len(a) + 1):
    #             print(dp[ii])

    # return "YES" if dp[len(a)][len(b)] else "NO"


if __name__ == "__main__":
    fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

    with open("./tc1") as fp:
        while line := fp.readline():
            q = int(line.strip())

            for q_itr in range(q):
                line = fp.readline()
                a = line.strip()

                line = fp.readline()
                b = line.strip()

                result = abbreviation(a, b)

                fptr.write(result + "\n")

            fptr.close()
