from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result =[]
        length = len(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            startIndex = i + 1
            endIndex = length-1
            target = nums[i] * -1
            while startIndex < endIndex:
                if nums[startIndex] + nums[endIndex] == target:
                    result.append([nums[i],nums[startIndex],nums[endIndex]])
                    startIndex = startIndex + 1
                    while startIndex < endIndex and nums[startIndex] == nums[startIndex - 1]:
                        startIndex = startIndex + 1
                elif nums[startIndex] + nums[endIndex] < target:
                    startIndex = startIndex + 1
                else:
                    endIndex = endIndex - 1
        return result





def main():
    arr = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(arr))


if __name__ == "__main__":
    main()
