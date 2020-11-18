from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            elm = nums[i]
            elmIndex = nums[i] - 1
            if elmIndex != i and nums[i] != nums[elmIndex]:
                temp = nums[i]
                nums[i] = nums[elmIndex]
                nums[elmIndex] = temp
            elif nums[i] == nums[elmIndex]:
                i = i+1
        result = []
        for i in range(len(nums)):
            elm = nums[i]
            elmIndex =elm -1
            if elmIndex != i:
                result.append(i+1)
        return result

nums = [4,3,2,7,8,2,3,1]

print(Solution().findDisappearedNumbers(nums))


