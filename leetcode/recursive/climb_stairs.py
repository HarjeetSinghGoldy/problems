class Solution:
    def climbStairs(self, n: int) -> int:
        targetStep = n
        dp = {}
        return self.recSolve(targetStep, dp)

    def recSolve(self, targetStep, dp):
        if targetStep == 0 or targetStep == 1:
            return 1
        if targetStep in dp:
            return dp[targetStep]
        else:
            result = self.recSolve(targetStep - 2, dp) + self.recSolve(targetStep - 1, dp)
            dp[targetStep] = result
            return dp[targetStep]


print(Solution().climbStairs(10))
