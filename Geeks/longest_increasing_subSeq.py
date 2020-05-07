def LISS(n, arr):
    # print(n, arr)
    lcarr = [1] * (n)
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                lcarr[i] = max(lcarr[i], lcarr[j] + 1)
    maxSub = 0
    for elm in lcarr:
        if elm > maxSub:
            maxSub = elm
    return maxSub


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(LISS(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
