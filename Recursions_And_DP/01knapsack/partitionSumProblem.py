from typing import List


class Solution:
    def canPartition(nums: List[int], ) -> bool:
        print(nums)
        numsSum = 0
        for elm in nums:
            numsSum = numsSum + elm
        if numsSum % 2 == 0:
            return bool(Solution.subsetSum(nums, int(numsSum / 2)))
        else:
            return False

    def subsetSum(nums, s):
        n = int(len(nums))
        rows, cols = (n + 1, s + 1)
        t = [[0] * cols for _ in range(rows)]

        for i in range(n + 1):
            for j in range(s + 1):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 1

        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if nums[i - 1] <= j:
                    t[i][j] = t[i - 1][j - nums[i - 1]] or t[i - 1][j]
                elif nums[i - 1] > j:
                    t[i][j] = t[i - 1][j]
        return t[n][s]


def main():
    inputs = list(map(int, input().strip().split()))
    # print(inputs)
    print(Solution.canPartition(inputs))


if __name__ == "__main__":
    main()
