#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    # print(f"{cost=}, {money=}")
    hm = {}

    for i, c in enumerate(cost):
        # print(f"{i=} {c=}")
        diff = money - c
        if c in hm:
            print(f"{hm[c]} {i+1}")
            return

        hm[diff] = i + 1


if __name__ == "__main__":
    with open("./in0") as fp:
        while line := fp.readline():
            t = int(line.strip())

            for t_itr in range(t):
                line = fp.readline()
                money = int(line)

                line = fp.readline()
                n = int(line)

                line = fp.readline()
                cost = list(map(int, line.rstrip().split()))

                whatFlavors(cost, money)
