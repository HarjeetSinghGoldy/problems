from typing import List


class Solution:
    def change(amount: int, coins: List[int]) -> int:
        print(amount, coins)
        return Solution.countSubsetSum(coins, amount)

    @classmethod
    def countSubsetSum(cls, a, s):
        n = len(a)
        rows, cols = (n + 1, s + 1)
        t = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 1

        for i in range(1,rows):
            for j in range(1,cols):
                if a[i - 1] <= j:
                    t[i][j] = t[i][j - a[i - 1]] + t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]
        return t[n][s]


def main():
    coins = list(map(int, input().strip().split()))
    amount = int(input())

    print(Solution.change(amount, coins))


if __name__ == "__main__":
    main()
