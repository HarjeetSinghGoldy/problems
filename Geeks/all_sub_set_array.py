def subArray(n, arr):
    subset = [-1] * n
    test = {}
    count = []
    helper(arr, subset, 0, test,count)
    print(test)
    print(len(count))
    returnStr = "NO"
    for elm in test:
        if test[elm] > 1:
            returnStr = "YES"
    return returnStr




def helper(arr, subset, i, test,count):
    if i == len(arr):
        # print(subset)
        count.append(subset.copy())
        tempSum = 0
        for elm in subset:
            if elm:
                tempSum += elm
        if tempSum not in test:
            test[tempSum] = 1
        else:
            test[tempSum] += 1
    else:
        subset[i] = None
        helper(arr, subset, i + 1, test,count)
        subset[i] = arr[i]
        helper(arr, subset, i + 1, test,count)


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(subArray(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
