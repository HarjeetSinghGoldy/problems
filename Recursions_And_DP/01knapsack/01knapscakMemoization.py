def knapsackO1(Wt, Val, C, n, t):
    if n == 0 or C == 0:
        t[n][C] = 0
        return 0
    if t[n][C] != -1:
        return t[n][C]
    if Wt[n - 1] <= C:
        t[n][C] = max(Val[n - 1] + knapsackO1(Wt, Val, C - Wt[n - 1], n - 1, t), knapsackO1(Wt, Val, C, n - 1, t))
        return t[n][C]
    elif Wt[n - 1] > C:
        t[n][C] = knapsackO1(Wt, Val, C, n - 1, t)
        return t[n][C]

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
        rows, cols = (n[0] + 1, C[0] + 1)
        # t = [[-1] * cols] * rows
        t = [[-1] * cols for _ in range(rows)]

        print(knapsackO1(Wt, Val, C[0], n[0], t))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
