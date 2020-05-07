import sys
from typing import List


class Solution:
    def lastStoneWeightII(stones: List[int]) -> int:
        stonesW = 0
        for elm in stones:
            stonesW = stonesW + elm

        filterStones = Solution.subSetSum(stones, int(stonesW / 2))

        minW = sys.maxsize
        for i in range(len(filterStones)):
            if filterStones[i] != 0:
                minW = min(minW, stonesW - 2 * i)
        return minW

    @classmethod
    def subSetSum(cls, a, s):
        n = len(a)
        rows, cols = (n + 1, s + 1)
        t = [[-1] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 1

        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if a[i - 1] <= j:
                    t[i][j] = t[i - 1][j - a[i - 1]] or t[i - 1][j]
                elif a[i - 1] > j:
                    t[i][j] = t[i - 1][j]
        return t[n]


def main():
    arr = list(map(int, input().strip().split()))
    print(Solution.lastStoneWeightII(arr))


if __name__ == "__main__":
    main()
