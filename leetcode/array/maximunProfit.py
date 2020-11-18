from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        maxOnRight = prices[-1]
        maxProfit = 0

        for i in reversed(range(len(prices) - 1)):
            if prices[i] < maxOnRight:
                maxProfit = max(maxProfit, maxOnRight - prices[i])
            else:
                maxOnRight = prices[i]
        return maxProfit


arr = [7, 1, 5, 3, 6, 4]
arr = [7,6,4,3,1]
arr = [2,1,1,1,1]
print(Solution().maxProfit(arr))
