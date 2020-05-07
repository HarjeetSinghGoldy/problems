def knapsackO1(Wt, Val, C, n, t):
    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if Wt[i - 1] <= j:
                t[i][j] = max(Val[i - 1] + t[i - 1][j - Wt[i - 1]], t[i - 1][j])
            elif Wt[i - 1] > j:
                t[i][j] = t[i - 1][j]
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
