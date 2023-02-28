#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    print(f"{expenditure=}, {d=}")
    res = 0

    # def getMedian(exp, l, r):
    #     tmp = sorted(expenditure[l : r + 1])
    #     mid = d // 2
    #     if d % 2 == 0:
    #         return (tmp[mid - 1] + tmp[mid]) / 2
    #     else:
    #         return tmp[mid]

    freq = {}

    def find(idx):
        print(f"{idx=}")
        s = 0
        for i in range(200):
            f = 0
            if i in freq:
                f = freq[i]
            s = s + f
            if s >= idx:
                return i

    for i in range(len(expenditure)):
        print(f"{i=}")
        freq[expenditure[i]] = freq.get(expenditure[i], 0) + 1
        print(f"{freq=}")
        if i >= d:
            freq[expenditure[i - d]] = freq.get(expenditure[i - d], 0) - 1
            print(f"{freq=}")
            median = find(d / 2 + d % 2)
            print(f"{median=}")
            if d % 2 == 0:
                ret = find(d / 2 + 1)
                if expenditure[i] >= median + ret:
                    res += 1
            else:
                if expenditure[i] >= median * 2:
                    res += 1

    # Write your code here
    return res


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    with open("./in0") as fp:
        while line := fp.readline():
            first_multiple_input = line.rstrip().split()

            n = int(first_multiple_input[0])

            d = int(first_multiple_input[1])

            line = fp.readline()
            expenditure = list(map(int, line.rstrip().split()))

            result = activityNotifications(expenditure, d)

            fptr.write(str(result) + "\n")

            fptr.close()
