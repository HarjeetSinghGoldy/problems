def odd_occ(n, arr):
    # print(n, arr)
    res = 0
    for i in range(n):
        res = res ^ arr[i]
    return res


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(odd_occ(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
