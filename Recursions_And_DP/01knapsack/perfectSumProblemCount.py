def knapsackO1(a, n, s, t):
    # print(a,n,s,t)
    for i in range(n + 1):
        for j in range(s + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if a[i - 1] <= j:
                t[i][j] = t[i - 1][j - a[i - 1]] + t[i - 1][j]
            elif a[i - 1] > j:
                t[i][j] = t[i - 1][j]
    return t[n][s]


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(3):
            inputs.append(input().strip().split())
        n = list(map(int, inputs[0]))
        arr = list(map(int, inputs[1]))
        s = list(map(int, inputs[2]))
        rows, cols = (n[0] + 1, s[0] + 1)
        t = [[-1] * cols for _ in range(rows)]
        print(knapsackO1(arr, n[0], s[0], t))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
