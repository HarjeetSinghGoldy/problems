import sys
import timeit
# from datetime import time
import time


class Solution:
    def minCut(s: str) -> int:
        # print(s)
        n = len(s)
        i = 0
        j = n - 1
        rc = n
        t = [[-1] * rc for _ in range(rc)]

        if Solution.isPalandrom(s, i, j):
            return 0

        for i in range(n):
            t[i][i] = 0

        for chain_length in range(1, n):
            for i in range(n - chain_length):
                j = i + chain_length
                # if t[i][j] == -1:
                if Solution.isPalandrom(s, i, j):
                    t[i][j] = 0
                    # print("Find palindromes",i,j)
                    continue
                minPart = n - 1
                for k in range(i, j):
                    tempPart = t[i][k] + t[k + 1][j] + 1
                    minPart = min(tempPart, minPart)
                t[i][j] = minPart
        # print(t)
        return t[0][n - 1]

    @classmethod
    def isPalandrom(cls, s, i, j):
        if i >= j:
            return 1
        while i < j:
            if s[i] != s[j]:
                return 0
            i += 1
            j -= 1
        return 1


def main():
    string = input()
    start = time.time()
    print("hello")
    print(Solution.minCut(string))
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
