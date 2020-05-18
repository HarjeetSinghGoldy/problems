import sys


def MCM(arr):
    n = len(arr)
    t = [[-1] * n for _ in range(n)]
    for i in range(1,n):
        t[i][i] = 0

    for chain in range(2, n+1):
        for i in range(1, n+1 - chain):
            j = i + chain - 1
            minMul = sys.maxsize
            for k in range(i, j):
                tempMul = t[i][k] + t[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                # print(tempMul, minMul)
                minMul = min(tempMul, minMul)
            t[i][j] = minMul
    print(t)
    return t[1][n]


def main():
    arr = list(map(int, input().strip().split()))
    print(MCM(arr))


if __name__ == "__main__":
    main()
