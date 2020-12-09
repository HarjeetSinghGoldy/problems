from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        n = len(height)
        if n <2:
            return 0
        i = 0
        j = n - 1

        while i < j:
            tempWater = min(height[i],height[j]) * (j-i)
            maxWater = max(maxWater,tempWater)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxWater

height = [1,8,6,2,5,4,8,3,7]
height = [1,1]

print(Solution().maxArea(height))



