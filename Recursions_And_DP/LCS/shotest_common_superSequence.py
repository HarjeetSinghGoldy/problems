class Solution:
    def shortestCommonSupersequence(str1: str, str2: str) -> str:
        # print(str1, str2)
        return Solution.lcs(str1, str2)

    @classmethod
    def lcs(cls, str1, str2):
        m = len(str1)
        n = len(str2)
        rows = m + 1
        cols = n + 1

        t = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    t[i][j] == 0
                if j == 0:
                    t[i][j] == 0
        for i in range(1, rows):
            for j in range(1, cols):
                if str1[i - 1] == str2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        return Solution.scsString(t, str1, str2, m, n)

    @classmethod
    def scsString(cls, t, str1, str2, i, j):
        scsString = ''
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                scsString = scsString + str1[i - 1]
                i -= 1
                j -= 1
            else:
                if t[i - 1][j] >= t[i][j - 1]:
                    scsString = scsString + str1[i - 1]
                    i = i - 1
                else:
                    scsString = scsString + str2[j - 1]
                    j = j - 1

        scsString = scsString[::-1]

        while i > 0:
            scsString = str1[i - 1] + scsString
            i -= 1
        while j > 0:
            scsString = str2[j - 1] + scsString
            j -= 1

        return scsString


def main():
    text1 = input()
    text2 = input()

    print(Solution.shortestCommonSupersequence(text1, text2))


if __name__ == "__main__":
    main()
