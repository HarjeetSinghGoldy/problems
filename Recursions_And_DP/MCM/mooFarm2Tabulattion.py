import sys


def Solve(arr, n, g, s):
    rc = n
    t = [[-1] * rc for _ in range(rc)]
    for i in range(n):
        t[i][i] = 0

    for chain_length in range(1, n):
        for i in range(n - chain_length):
            j = i + chain_length
            if s == 0:
                if i == j:
                    t[i][j] = 0
                else:
                    t[i][j] = arr[j] * arr[j] - arr[i] * arr[i]
                continue
            minSum = sys.maxsize
            for k in range(i, j):
                s = s - 1
                tempPart = arr[k] * arr[k] - arr[i] * arr[i] + t[k + 1][j]
                minSum = min(tempPart, minSum)
            t[i][j] = minSum
    return t[0][n - g]


def MoonFarm(arr, n, k):
    # print(arr, n, k)
    s = k - 1
    return Solve(arr, n, k, s)


def main():
    testCase = int(input())
    while testCase > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        first = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(MoonFarm(arr, first[0], first[1]))
        testCase -= 1


if __name__ == "__main__":
    main()
