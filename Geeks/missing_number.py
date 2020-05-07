def missing_number(n, arr):
    sumOfNumbers = 0
    sumOfNumbers = n*(n+1)/2

    for elm in arr:
        sumOfNumbers = sumOfNumbers - elm

    return int(sumOfNumbers)

def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        # print(inputs)
        length = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        print(missing_number(length[0], arr))
        testCases = testCases - 1

if __name__ == "__main__":
    main()
