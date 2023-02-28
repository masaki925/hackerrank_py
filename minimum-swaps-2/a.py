#!env python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    res = 0

    #  0, 1, 2, 3, 4, 5, 6
    # [7, 1, 3, 2, 4, 5, 6]

    #  0, 1, 2, 3, 4
    # [2, 3, 4, 1, 5]
    # (1, 2)
    #    (2, 3)
    #       (3, 4)
    #          (4, 1)
    #             (5, 5)

    # (1, 2)
    #    (2, 1)
    #       (3, 4)
    #          (4, 3)
    #             (5, 5)

    # (1, 1)
    #    (2, 2)
    #       (3, 4)
    #          (4, 3)
    #             (5, 5)

    # (1, 1)
    #    (2, 2)
    #       (3, 3)
    #          (4, 4)
    #             (5, 5)

    for i in range(len(arr)):
        while arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            res += 1

    # for i in range(len(arr)):
    #     # print(f"{i=}")
    #     # print(f"{arr=}")
    #     if arr[i] - 1 != i:
    #         cand = arr[arr[i] - 1]
    #         # print(f"{cand=}")

    #         if cand - 1 != i:
    #             # search complete swap
    #             for j in range(i + 1, len(arr)):
    #                 if arr[j] - 1 == i:
    #                     # print(f"{i=}, {j=}")
    #                     tmp = arr[j]
    #                     arr[j] = arr[arr[i] - 1]
    #                     arr[arr[i] - 1] = tmp
    #                     # print(f"{arr=}")
    #                     res += 1
    #                     break

    #         # do swap
    #         # print(f"{i=}, {arr[i] - 1=}")
    #         tmp = arr[i]
    #         arr[i] = arr[tmp - 1]
    #         arr[tmp - 1] = tmp
    #         # print(f"{arr=}")
    #         res += 1

    return res


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    # fptr = open("./out", "w")

    with open("./in") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            n = int(line.strip())

            line = fp.readline()
            arr = list(map(int, line.split()))

            res = minimumSwaps(arr)
            print(f"{res=}")

            # fptr.write(str(res) + "\n")

            # fptr.close()

# [7,1,2,3,4,5,6]
# (1, 7)
#   (2, 1)
#     (3, 2)
#       (4, 3)
#         (5, 4)
#           (6, 5)
#             (7, 6)

# (1, 6)
#   (2, 1)
#     (3, 2)
#       (4, 3)
#         (5, 4)
#           (6, 5)
#             (7, 7)

# (1, 5)
#   (2, 1)
#     (3, 2)
#       (4, 3)
#         (5, 4)
#           (6, 6)
#             (7, 7)

# (1, 4)
#   (2, 1)
#     (3, 2)
#       (4, 3)
#         (5, 5)
#           (6, 6)
#             (7, 7)

# (1, 3)
#   (2, 1)
#     (3, 2)
#       (4, 4)
#         (5, 5)
#           (6, 6)
#             (7, 7)

# (1, 2)
#   (2, 1)
#     (3, 3)
#       (4, 4)
#         (5, 5)
#           (6, 6)
#             (7, 7)
