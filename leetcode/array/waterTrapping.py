from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [-1] * len(height)
        maxRight = [-1] * len(height)
        maxLeft[0] = (height[0])
        maxRight[len(height) - 1] = height[len(height) - 1]
        totalWater = 0

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        water = [0] * len(height)

        for i in range(len(height)):
            water[i] = min(maxLeft[i],maxRight[i]) - height[i]

        for i in range(len(height)):
            totalWater = totalWater + water[i]

        return totalWater


h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution().trap(h))
