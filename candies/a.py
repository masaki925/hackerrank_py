#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def candies(n, arr):
    print(f"{n=}, {arr=}")

    # 4 6 4 3 4 1
    #
    # [4]
    # [4, 6]
    # [4] => 6, 2
    # [] => 4, 1
    # [4]
    # [] => 4, 1
    #
    # 1, 3, 2, 1, 2, 1
    #
    #####################
    # 4 6 4 5 6 2
    # [4]
    # [4, 6]
    # [4] => 6, 2
    # [] => 4, 1
    # [4]
    # [4, 5]
    # [4, 5, 6]
    # [4, 5] => 6, 3
    # [4] => 5, 2
    # [] => 4, 1
    # [2]
    # [] => 2, 1
    #
    # 1 2 1 2 3 1

    res = [1] * len(arr)

    for i, num in enumerate(arr):
        print(f"{i=}")
        tmp = 1
        cur = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < cur:
            tmp += 1
            cur = arr[j]
            j -= 1
        print(f"{tmp=}")

        j = i + 1
        tmp2 = 1
        cur = arr[i]
        while j < len(arr) and arr[j] < cur:
            print(f"{arr[j]=}, {arr[i]=}")
            tmp2 += 1
            cur = arr[j]
            j += 1
        print(f"{tmp2=}")

        res[i] = max(tmp, tmp2)

    return sum(res)


if __name__ == "__main__":
    fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

    with open("./tc0") as fp:
        while line := fp.readline():
            n = int(line.strip())

            arr = []

            for _ in range(n):
                line = fp.readline()
                arr_item = int(line.strip())
                arr.append(arr_item)

            result = candies(n, arr)

            fptr.write(str(result) + "\n")

            fptr.close()
