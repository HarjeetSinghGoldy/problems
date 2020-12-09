from typing import List


class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        resultList = [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target and resultList[0] == -1:
                resultList[0] = i
                resultList[1] = i
            elif nums[i] == target and resultList[0] != -1:
                resultList[1] = i

        return resultList

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.binarySearch(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        right_index = self.binarySearch(nums, target, False) - 1

        return [left_index, right_index]

    def binarySearch(self, nums, target, flag):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (flag and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low


nums = [5, 7, 7, 8, 8, 10]
target = 8
#
# nums = [5, 7, 7, 8, 8, 10]
# target = 6
# nums = []
# target = 0

print(Solution().searchRange(nums, target))
