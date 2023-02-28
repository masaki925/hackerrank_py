#!env python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    print(f"{queries=}")
    res = []
    hm = {}
    freq = {}

    for q in queries:
        if q[0] == 1:
            if q[1] not in hm:
                hm[q[1]] = 0
            else:
                freq[hm[q[1]]] = max(0, freq[hm[q[1]]] - 1)

            # insert
            hm[q[1]] += 1

            freq[hm[q[1]]] = freq.get(hm[q[1]], 0) + 1
        elif q[0] == 2:
            if q[1] not in hm:
                continue

            freq[hm[q[1]]] = max(0, freq[hm[q[1]]] - 1)

            # delete
            hm[q[1]] -= 1

            freq[hm[q[1]]] = freq.get(hm[q[1]], 0) + 1
        else:
            if q[1] in freq and freq[q[1]]:
                res.append(1)
            else:
                res.append(0)

    return res


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    with open("./in2") as fp:
        while line := fp.readline():
            q = int(line.strip())

            queries = []

            for _ in range(q):
                line = fp.readline()
                queries.append(list(map(int, line.rstrip().split())))

            ans = freqQuery(queries)

            fptr.write("\n".join(map(str, ans)))
            fptr.write("\n")

            fptr.close()
