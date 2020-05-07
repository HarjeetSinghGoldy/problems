def minSteps(length, arr):
    # print(length, arr)
    stepCount = 0
    while 1:
        zeroCount = 0
        i = 0
        for elm in arr:
            # print(type(elm),elm)
            if elm & 1:  # if odd break the loop
                break
            elif elm == 0:
                zeroCount += 1
            i += 1

        if zeroCount == length:
            return stepCount
        if i == length:  # all numbers are even
            for j in range(length):
                arr[j] = int(arr[j] / 2)
            stepCount += 1
        for k in range(i,length):
            if arr[k] & 1:
                arr[k] -= 1
                stepCount += 1

def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(minSteps(length[0], arr))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
