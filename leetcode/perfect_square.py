class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = []
        i = 1
        while True:
            pNumber = i * i
            if pNumber <= n:
                perfectSquares.append(pNumber)
                i = i + 1
            else:
                break
        hashMem = {}
        dp = [n] * (n + 1)
        for i in range(4):
            dp[i] = i
        # return self.recSolve(n, perfectSquares,hashMem)
        return self.recSolve2(n, perfectSquares,dp)

    def recSolve(self, n, perfectSquares,hashMem):
        if n < 4:
            return n
        count = n
        if n in hashMem:
            return hashMem[n]
        for i in range(len(perfectSquares)):
            reducedN = n - perfectSquares[i]
            if reducedN >= 0:
                count = min(count, self.recSolve(reducedN, perfectSquares,hashMem) + 1)
                hashMem[n] = count
        return count

    def recSolve2(self, n, perfectSquares,dp):
        for i in range(4,n+1):
            for j in range(len(perfectSquares)):
                perfectSquaresVal = perfectSquares[j]
                dp[i] = min(dp[i], dp[i - perfectSquaresVal]+1)

        return dp[n]
n = 12

print(Solution().numSquares(n))
