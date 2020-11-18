from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumList = []
        tempNum = 0
        for num in nums:
            tempNum = tempNum + num
            sumList.append(tempNum)

        result = sumList[k-1] / k
        for i in range(k,len(nums)):
            result = max(result, ((sumList[i]-sumList[i-k])/k))
        return result



nums = [1, 12, -5, -6, 50, 3]
k = 4
# nums = [5]
# k=1
print(Solution().findMaxAverage(nums, k))
