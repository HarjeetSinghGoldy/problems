def lcs(str1, str2, m, n, t):
    for i in range(m+1):
        for j in range(n+1):
            if i ==0:
                t[i][j] == 0
            if j ==0:
                t[i][j] == 0

    for i in range(1,m + 1):
        for j in range(1,n + 1):
            if str1[i - 1] == str2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    return t[m][n]


def minDelInsStr(str1, str2, m, n, t):
    lo = lcs(str1, str2, m, n, t)
    minDel = m - lo
    minIns = n - lo
    # print(lo, minIns,minDel)
    return minDel + minIns


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        for i in range(2):
            inputs.append(input().strip().split())
        lengths = list(map(int, inputs[0]))
        strings = list(inputs[1])
        rows, cols = (lengths[0] + 1, lengths[1] + 1)
        t = [[0] * cols for _ in range(rows)]
        print(minDelInsStr(strings[0], strings[1], lengths[0], lengths[1], t))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
