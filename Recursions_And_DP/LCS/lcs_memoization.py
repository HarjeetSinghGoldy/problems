class Solution:
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # print(text1, text2, m, n)
        cols, rows = n + 1, m + 1
        t = [[-1] * cols for _ in range(rows)]
        return Solution.LCS(text1, text2, m, n, t)

    @classmethod
    def LCS(cls, text1, text2, m, n, t):
        if m == 0 or n == 0:
            return 0
        if t[m][n] != -1:
            return t[m][n]
        if text1[m - 1] == text2[n - 1]:
            t[m][n] = 1 + Solution.LCS(text1, text2, m - 1, n - 1,t)
            return t[m][n]
        else:
            t[m][n] = max(Solution.LCS(text1, text2, m - 1, n,t), Solution.LCS(text1, text2, m, n - 1,t))
            return t[m][n]


def main():
    text1 = input()
    text2 = input()

    print(Solution.longestCommonSubsequence(text1, text2))


if __name__ == "__main__":
    main()
