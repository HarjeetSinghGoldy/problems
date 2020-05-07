def majority_elm(n, arr):
    # print(n, arr)
    count = 1
    majElmIndex = 0

    for i in range(1, n):
        if arr[majElmIndex] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majElmIndex = i
            count = 1

    elmN = 0
    for i in range(n):
        if arr[majElmIndex] == arr[i]:
            elmN += 1

    if elmN > n / 2:
        return arr[majElmIndex]
    else:
        return -1


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(majority_elm(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
