import sys
sys.setrecursionlimit(10 ** 6)
class Solution:
    def superEggDrop(self, e: int, f: int) -> int:
        rows = e + 1
        cols = f + 1
        t = [[-1] * cols for _ in range(rows)]
        return Solution.recursiveHelper(e, f, t)

    @classmethod
    def recursiveHelper(cls, e, f, t):
        if f == 0 or f == 1:
            t[e][f] = f
            return f
        if e == 1:
            t[e][f] = f
            return f
        if t[e][f] != -1:
            # print("reuse")
            return t[e][f]
        minMove = sys.maxsize
        for k in range(1, f + 1):
            if t[e - 1][k - 1] != -1:
                # print("reuse  low")
                lowFloor = t[e - 1][k - 1]
            else:
                t[e-1][k-1] = Solution.recursiveHelper(e - 1, k - 1, t)
                lowFloor = t[e-1][k-1]
            if t[e][f - k] != -1:
                # print("reuse  high")
                highFloor = t[e][f - k]
            else:
                t[e][f - k] = Solution.recursiveHelper(e, f - k, t)
                highFloor = t[e][f - k]

            tempMove = 1 + max(highFloor, lowFloor)
            minMove = min(tempMove, minMove)
        t[e][f] = minMove
        return t[e][f]


def main(self=None):
    e = int(input())
    f = int(input())
    print(Solution.superEggDrop(self, e, f))


if __name__ == "__main__":
    main()
