def sumCount(length, sum, arr):
    # print(length,sum,arr)
    elmmap = {}
    for i in range(length):
        if not arr[i] in elmmap:
            elmmap[arr[i]] =1
        else:
            elmmap[arr[i]] = elmmap[arr[i]] +1
    twice_count = 0
    print(elmmap)
    for i in range(length):
        if sum - arr[i] > 0:
            twice_count = twice_count + elmmap[sum - arr[i]]
            if  sum - arr[i] == arr[i]:
                twice_count = twice_count -1

    return int(twice_count/2)

def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(sumCount(length[0],length[1],arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
