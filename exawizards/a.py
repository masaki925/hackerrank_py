import sys

from collections import Counter


def findLove(w, l):
    print(f"{w=}, {l=}")
    res = 0

    wc = Counter(w)
    l = set(l)

    for word in set(l):
        cnt = Counter(word)
        if wc.keys() == cnt.keys():
            print(f"{word=}")
            res += 1

    return res


if __name__ == "__main__":
    fptr = sys.stdout

    with open("./in") as fp:
        while line := fp.readline():
            # t = int(input().strip())
            w = line.strip()

            line = fp.readline()
            l = line.strip().split()
            # l = int(input().strip())

            result = findLove(w, l)

            fptr.write(str(result) + "\n")

            fptr.close()
