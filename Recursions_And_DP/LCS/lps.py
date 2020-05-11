class Solution:
    def longestPalindromeSubseq(s: str) -> int:
        revStr = s[::-1]
        m = len(s)
        rc = m + 1
        t = [[0] * rc for _ in range(rc)]

        return Solution.lps(s, revStr, m, t)

    @classmethod
    def lps(cls, s, revStr, m, t):
        # print(s,revStr)
        for i in range(m + 1):
            for j in range(m + 1):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 0
        for i in range(1,m + 1):
            for j in range(1,m + 1):
                if s[i - 1] == revStr[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])
        return t[m][m]


def main():
    strA = input()

    print(Solution.longestPalindromeSubseq(strA))


if __name__ == "__main__":
    main()
