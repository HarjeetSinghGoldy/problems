# Leetcode target sum problem
from typing import List
class Solution:
    def findTargetSumWays(nums: List[int], diff: int) -> int:
        # print(nums, S)
        Sum = 0
        a = [None]*(len(nums)+1)
        for i in range(len(nums)):
            a[i + 1] = nums[i]
            Sum = Sum + nums[i]
        if diff > Sum:
            return 0
        if (diff - Sum) & 1:
            return 0
        S2 = int((Sum + diff) / 2)
        return Solution.SubSetSumCount(nums, S2, a)

    @classmethod
    def SubSetSumCount(cls, nums, s, a):
        n = len(nums)
        rows = n + 1
        cols = s + 1
        t = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 1
        for i in range(1, rows):
            if a[i] == 0:
                t[i][0] = 2 * t[i - 1][0]
            else:
                t[i][0] = t[i - 1][0]

        for i in range(1, rows):
            for j in range(1, cols):
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j - nums[i - 1]] + t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]
        return t[n][s]


def main():
    arr = list(map(int, input().strip().split()))
    S = int(input())
    print(Solution.findTargetSumWays(arr, S))


if __name__ == "__main__":
    main()
