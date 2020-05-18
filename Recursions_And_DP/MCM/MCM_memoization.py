import sys

def mcmRecusive(arr, i, j, t):
    if i >= j:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    minMul = sys.maxsize
    for k in range(i, j):
        tempRes = mcmRecusive(arr, i, k, t) + mcmRecusive(arr, k + 1, j, t) + arr[i - 1] * arr[k] * arr[j]
        if minMul > tempRes:
            minMul = tempRes
    t[i][j] = tempRes
    return t[i][j]


def MCM(arr, arrSize):
    # print(arr, arrSize)
    # rc = arrSize + 1
    rc = 1000 + 1
    t = [[-1] * rc for _ in range(rc)]
    i = 1
    j = arrSize - 1
    return mcmRecusive(arr, i, j, t)


def main():
    testCase = int(input())
    while testCase > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        arrSize = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(MCM(arr, arrSize[0]))
        testCase -= 1


if __name__ == "__main__":
    main()
