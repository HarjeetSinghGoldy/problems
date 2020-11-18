from typing import List


class Solution:
    def maxSumConsecutive(self,nums:List[int])->List:
        currentNum = nums[0]
        maxSum = nums[0]
        for i in range(1,len(nums)):
            currentNum = max(currentNum,currentNum+nums[i])
            if currentNum > maxSum:
                maxSum = currentNum

        return maxSum

