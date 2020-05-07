def leaders(n, arr):
    max_number_right = arr[n - 1]
    arr[n - 1] = -1
    for i in range(n - 2, -1, -1):
        temp = arr[i]
        arr[i] = max_number_right
        if max_number_right< temp:
            max_number_right = temp
    # listToStr = ' '.join([str(elem) for elem in reversed(max_numbers)])
    listToStr = ' '.join([str(elm) for elm in arr])
    return listToStr


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(leaders(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
