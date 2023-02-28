#!env python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def areAnagrams(str1, str2):
    # Create arrays to store the frequency of each letter
    freq1 = [0] * 26
    freq2 = [0] * 26

    # Iterate through both strings and update the frequency arrays
    for i in range(len(str1)):
        freq1[ord(str1[i]) - ord("a")] += 1
    for i in range(len(str2)):
        freq2[ord(str2[i]) - ord("a")] += 1

    # Check if the frequency arrays are equal
    for i in range(26):
        if freq1[i] != freq2[i]:
            return False

    return True


def sherlockAndAnagrams(s):
    # Initialize a counter to store the number of anagrammatic pairs
    count = 0

    # Iterate through all possible pairs of substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # Iterate through all possible overlaps of the second substring
            for k in range(j, len(s) + 1):
                # Check if the substrings are anagrams of each other
                if areAnagrams(s[i:j], s[j - k : k]):
                    count += 1

    return count


if __name__ == "__main__":
    fptr = sys.stdout  # open(os.environ["OUTPUT_PATH"], "w")

    with open("./in") as fp:
        while line := fp.readline():
            q = int(line.strip())

            for q_itr in range(q):
                line = fp.readline()
                s = line.strip()

                result = sherlockAndAnagrams(s)

                fptr.write(str(result) + "\n")

            fptr.close()
