#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def checkMagazine(magazine, note):
    # print(f"{magazine=}, {note=}")
    hm1 = {}
    hm2 = {}

    for w in magazine:
        hm1[w] = hm1.get(w, 0) + 1

    for w in note:
        hm2[w] = hm2.get(w, 0) + 1

    for w in note:
        if (w not in hm1) or (hm1[w] < hm2[w]):
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    with open("./tc0") as fp:
        while line := fp.readline():
            first_multiple_input = line.rstrip().split()

            m = int(first_multiple_input[0])

            n = int(first_multiple_input[1])

            line = fp.readline()
            magazine = line.rstrip().split()

            line = fp.readline()
            note = line.rstrip().split()

            checkMagazine(magazine, note)
