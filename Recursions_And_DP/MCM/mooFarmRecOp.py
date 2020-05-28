import sys


def Solve(arr, n, i, j, s):
    if i >= j:
        return 0
    if s == 0:
        if i == j:
            return 0
        else:
            return arr[j] * arr[j] - arr[i] * arr[i]
    minSum = sys.maxsize
    for k in range(i, j):
        temp = arr[k] * arr[k] - arr[i] * arr[i] + Solve(arr, n, k + 1, j, s - 1)
        minSum = min(temp, minSum)
    return minSum


def MoonFarm(arr, n, k):
    print(arr, n, k)
    i = 0
    j = n - 1
    s = k - 1
    return Solve(arr, n, i, j, s)


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
