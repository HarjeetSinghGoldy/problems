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
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        i, j = m, n
        lcsString = ''
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                lcsString = lcsString + text1[i - 1]
                i -= 1
                j -= 1
            else:
                if t[i - 1][j] > t[i][j - 1]:
                    i = i - 1
                else:
                    j = j - 1

        return lcsString[::-1]


def main():
    text1 = input()
    text2 = input()

    print(Solution.longestCommonSubsequence(text1, text2))


if __name__ == "__main__":
    main()
