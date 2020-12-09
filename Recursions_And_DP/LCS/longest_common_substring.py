def lcssHelper(text1, text2, m, n, t):
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = 0
    maxValue = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if t[i][j] > maxValue:
                maxValue = t[i][j]

    return maxValue


def lcss(text1, text2, m, n, t):
    return lcssHelper(text1, text2, m, n, t)


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(3):
            inputs.append(input().strip().split())
        sizes = list(map(int, inputs[0]))
        text1 = inputs[1]
        text2 = inputs[2]
        rows, cols = (sizes[0] + 1, sizes[1] + 1)
        t = [[-1] * cols for _ in range(rows)]
        print(lcss(text1[0], text2[0], sizes[0], sizes[1], t))
        testCases = testCases - 1


if __name__ == "__main__":
    main()