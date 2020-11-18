def kadaneFunction(n, arr):
    print(n, arr)
    cur = arr[0]
    maxSum = arr[0]
    for i in range(1,n):
        cur = max(arr[i], cur+arr[i])
        if maxSum < cur:
            maxSum = cur
    return maxSum




def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(kadaneFunction(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
