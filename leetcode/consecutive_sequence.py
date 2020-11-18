from typing import List


class Solution:
    def longestConsecutiveBrute(self, nums: List[int]) -> int:
        longestStreak = 0
        for num in nums:
            currentNum = num
            currentStreak = 1
            while currentNum + 1 in nums:
                currentNum = currentNum + 1
                currentStreak += 1

            longestStreak = max(currentStreak, longestStreak)

        return longestStreak

    def longestConsecutiveHash(self,nums:List[int])-> int:
        longestStreak = 0
        hashMap = set(nums)

        for num in hashMap:
            if num - 1 not in hashMap:
                currentStreak = 1
                currentNum = num
                while currentNum + 1 in hashMap:
                    currentNum +=1
                    currentStreak +=1
                longestStreak = max(longestStreak, currentStreak)

        return longestStreak


    def longestConsecutiveSort(self, nums:List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longestStreak = 1
        currentStreak = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    currentStreak += 1
                else:
                    longestStreak = max(longestStreak,currentStreak)
                    currentStreak = 1
        return max(longestStreak,currentStreak)




# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutiveBrute(nums))
print(Solution().longestConsecutiveSort(nums))
print(Solution().longestConsecutiveHash(nums))