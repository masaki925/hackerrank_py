#!env python3

import math
import os
import random
import re
import sys


# Complete the minTime function below.
def minTime(machines, goal):
    # print(f"{machines=}, {goal=}")
    l, r = 0, min(machines) * goal
    res = r

    while l <= r:
        mid = (l + r) // 2
        # print(f"{l=}, {r=}, {mid=}")
        num_of_products = 0
        for m in machines:
            num_of_products += mid // m

        # print(f"{num_of_products=}")
        if num_of_products >= goal:
            r = mid - 1
            res = mid
        else:
            l = mid + 1

    return res


if __name__ == "__main__":
    fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

    with open("./in2", "r") as fp:
        while line := fp.readline():
            nGoal = line.split()  # input().split()

            n = int(nGoal[0])

            goal = int(nGoal[1])

            line = fp.readline()
            machines = list(map(int, line.rstrip().split()))

            ans = minTime(machines, goal)

    fptr.write(str(ans) + "\n")

    fptr.close()
