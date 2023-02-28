#!env python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    print(f"{arr=}, {r=}")

    # 与えられた数列の中にターゲットがあったら1 を返す
    # ベースケース
    #   トリプレットが作れた => 1
    #   i がlen(arr) をはみ出た => 0
    # イテレーション
    #   arr[i..n] を調べる
    #     ターゲットが0の場合:
    #       arr[i] mod 3 の場合:
    #         arr[j] を決断..
    #     ターゲット>0場合:
    #       arr[j] がターゲットの場合:
    #         arr[j] を決断記録に追加して、i + 1, arr[i] * 3 を探す

    # backtrack(i, target)
    arr = [x for x in arr if x == 1 or x % r == 0]
    sub = []

    def backtrack(i, target):
        print(f"{i=}, {target=}")
        if len(sub) == 3:
            return 1
        if i >= len(arr):
            return 0

        _res = 0
        for j in range(i, len(arr)):
            if len(sub) == 0:
                if arr[j] == 1 or arr[j] % r == 0:
                    sub.append(j)
                    _res += backtrack(j + 1, arr[j] * r)
                    sub.pop()
            else:
                if arr[j] == target:
                    sub.append(j)
                    _res += backtrack(j + 1, arr[j] * r)
                    sub.pop()

        return _res

    return backtrack(0, 0)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    fptr = sys.stdout

    with open("./in1") as fp:
        while line := fp.readline():
            nr = line.rstrip().split()

            n = int(nr[0])

            r = int(nr[1])

            line = fp.readline()
            arr = list(map(int, line.rstrip().split()))

            ans = countTriplets(arr, r)

            fptr.write(str(ans) + "\n")

            fptr.close()
