import sys
import time

class Solution:
    def minCut(s: str) -> int:
        # print(s)
        i = 0
        length = len(s)
        j = length - 1
        t = [[-1] * length for _ in range(length)]
        return Solution.helper(s, i, j, t)

    @classmethod
    def helper(cls, s, i, j, t):
        if i >= j:
            t[i][j] = 0
            return 0
        if t[i][j] != -1:
            return t[i][j]
        if Solution.isPalandrom(s, i, j):
            t[i][j] = 0
            return 0
        minPart = sys.maxsize
        for k in range(i, j):
            if t[i][k] != -1:
                left = t[i][k]
            else:
                left = Solution.helper(s, i, k, t)
            if t[k + 1][j] != -1:
                right = t[k + 1][j]
            else:
                right = Solution.helper(s, k + 1, j, t)
            tempPart = left + right + 1
            minPart = min(minPart, tempPart)
        t[i][j] = minPart
        return t[i][j]

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
