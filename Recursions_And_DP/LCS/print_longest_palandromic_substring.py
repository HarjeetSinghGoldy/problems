class Solution:
    def longestPalindrome(self,s: str) -> str:

        lpsLength = Solution.lps(s)

        return lpsLength

    @classmethod
    def lps(cls, s):
        sr = s[::-1]
        m = len(s)
        rc = m + 1
        t = [[0] * rc for _ in range(rc)]

        for i in range(rc):
            for j in range(rc):
                if i == 0:
                    t[i][j] == 0
                if j == 0:
                    t[i][j] == 0

        for i in range(1, rc):
            for j in range(1, rc):
                if s[i - 1] == sr[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    # t[i][j] = max(t[i-1][j],t[i][j-1])
                    t[i][j] = 0
        x = 0
        y = 0
        maxValue = 0
        for i in range(rc):
            for j in range(rc):
                if t[i][j] > maxValue:
                    x,y = i,j
                    maxValue = t[i][j]

        print(maxValue)
        lcsString = ''
        while x > 0 or y > 0:
            if s[x - 1] == sr[y - 1]:
                lcsString = lcsString + s[x - 1]
                x -= 1
                y -= 1
            else:
                if t[x - 1][y] > t[x][y - 1]:
                    x -= 1
                else:
                    y -= 1
        print(lcsString[::-1])
        return lcsString[::-1]

s = "caba"

Solution().longestPalindrome(s)
