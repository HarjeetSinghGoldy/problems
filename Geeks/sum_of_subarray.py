def minTimeFun(n, arr):
    if (n <= 0): return 0

    incl = arr[0]
    excl = 0

    for i in range(1, n):
        incl_new = arr[i] + min(excl, incl)
        excl_new = incl
        incl = incl_new
        excl = excl_new
    return min(incl, excl)


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(minTimeFun(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
