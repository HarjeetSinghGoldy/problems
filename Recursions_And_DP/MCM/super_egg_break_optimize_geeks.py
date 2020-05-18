import sys

class Solution:
    def superEggDrop(self, e: int, f: int) -> int:
        rows = e + 1
        cols = f + 1
        t = [[-1] * cols for _ in range(rows)]
        for i in range(rows):
            t[i][1] = 1  # // one trial for one floor
            t[i][0] = 0  # // zero trail for zero floor
            for j in range(cols):
                t[1][j] = j  # We always need j trials for one egg and j floors.
                t[0][j] = 0

        for i in range(2, rows):
            for j in range(2, cols):
                t[i][j] = sys.maxsize
                for k in range(1, j + 1):
                    tempFloor = 1 + max(t[i - 1][k - 1], t[i][j - k])
                    t[i][j] = min(tempFloor, t[i][j])

        return t[e][f]


def main(self=None):
    e = int(input())
    f = int(input())
    print(Solution.superEggDrop(self, e, f))


if __name__ == "__main__":
    main()
