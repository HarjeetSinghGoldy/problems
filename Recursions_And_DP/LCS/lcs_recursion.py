
class Solution:
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # print(text1, text2, m, n)
        return Solution.LCS(text1, text2, m, n)

    @classmethod
    def LCS(cls,text1, text2, m, n):
        if m == 0 or n == 0:
            return 0
        if text1[m - 1] == text2[n - 1]:
            return 1 + Solution.LCS(text1, text2, m - 1, n - 1)
        else:
            return max(Solution.LCS(text1, text2, m - 1, n), Solution.LCS(text1, text2, m, n - 1))


def main():
    text1 = input()
    text2 = input()

    print(Solution.longestCommonSubsequence(text1, text2))


if __name__ == "__main__":
    main()
