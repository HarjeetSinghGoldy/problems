import sys
from typing import List


class Solution:
    def coinChange(coins: List[int], amount: int) -> int:
        # print(coins, amount)
        return Solution.unboundedKnapSackCount(coins, amount)

    @classmethod
    def unboundedKnapSackCount(cls, coins, s):
        # print(coins, s)
        n = len(coins)
        rows, cols = (n + 1, s + 1)
        t = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    t[i][j] = sys.maxsize - 1
                if j == 0:
                    t[i][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if coins[i - 1] <= j:
                    t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]
        return -1 if t[n][s] >= sys.maxsize - 1 else t[n][s]


def main():
    coins = list(map(int, input().strip().split()))
    total = int(input())

    print(Solution.coinChange(coins, total))


if __name__ == "__main__":
    main()
