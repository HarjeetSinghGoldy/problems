def knapsackO1(Wt, Val, C, n):
    # print(Wt, Val, C, n)
    if n == 0 or C == 0:
        return 0
    if Wt[n - 1] <= C:
        return max(Val[n - 1] + knapsackO1(Wt, Val, C - Wt[n - 1], n - 1), knapsackO1(Wt, Val, C, n - 1))
    elif Wt[n - 1] > C:
        return knapsackO1(Wt, Val, C, n - 1)


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(4):
            inputs.append(input().strip().split())
        # print(inputs)
        n = list(map(int, inputs[0]))
        C = list(map(int, inputs[1]))
        Val = list(map(int, inputs[2]))
        Wt = list(map(int, inputs[3]))
        print(knapsackO1(Wt, Val, C[0], n[0]))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
