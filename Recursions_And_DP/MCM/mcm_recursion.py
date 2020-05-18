import sys


def MCMhelper(arr, i, j):
    if i >= j:
        return 0
    minMul = sys.maxsize
    for k in range(i, j):
        temp = MCMhelper(arr, i, k) + MCMhelper(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        minMul = min(minMul, temp)
    return minMul


def MCM(arr, length):
    # print(arr, length)
    i = 1
    j = len(arr) - 1
    return MCMhelper(arr, i, j)


def main():
    testCase = int(input())
    while testCase > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(MCM(arr, length[0]))
        testCase -= 1


if __name__ == "__main__":
    main()
