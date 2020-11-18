from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSideProduct = [0]*n
        rightSideProduct = [0]*n
        answers = [0]*n
        leftSideProduct[0] = 1
        rightSideProduct[n-1] = 1

        for i in range(1,n):
            leftSideProduct[i] = leftSideProduct[i-1]*nums[i-1]

        for i in reversed(range(n-1)):
            rightSideProduct[i] = rightSideProduct[i + 1] * nums[i + 1]

        for i in range(n):
            answers[i] = leftSideProduct[i]*rightSideProduct[i]

        return answers





nums = [1,2,3,4]

print(Solution().productExceptSelf(nums))
