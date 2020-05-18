import sys
from typing import List


class Solution:
    def maxCoins(nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.insert(len(nums) + 1, 1)
        n = len(nums)
        i = 1
        j = n - 1
        rc = n + 1
        t = [[-1] * rc for _ in range(rc)]
        return Solution.MCMmax(nums, i, j, t)

    @classmethod
    def MCMmax(cls, nums, i, j, t):
        if i >= j:
            return 0
        if t[i][j] != -1:
            return t[i][j]
        maxRes = -sys.maxsize
        for k in range(i, j):
            tempRes = Solution.MCMmax(nums, i, k, t) + Solution.MCMmax(nums, k + 1, j, t) + nums[i - 1] * nums[k] * \
                      nums[j]
            maxRes = max(maxRes, tempRes)
        t[i][j] = maxRes
        return t[i][j]


def main():
    nums = list(map(int, input().strip().split()))
    print(Solution.maxCoins(nums))


if __name__ == "__main__":
    main()
