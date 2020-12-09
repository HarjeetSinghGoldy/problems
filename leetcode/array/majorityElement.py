from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        n = len(nums)
        mElmCri = n/2
        mElm = -1


        for i in range(n):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] = hashMap[nums[i]] + 1

        for key in hashMap:
            if hashMap[key] > mElmCri:
                mElm = key
        return mElm





arr = [2,2,1,1,1,2,2]
arr = [3,2,3]

print(Solution().majorityElement(arr))

