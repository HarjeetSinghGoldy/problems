def reverseString(string):
    # print(string)
    l = 0
    r = len(string) - 1

    while (l < r):
        if specialCharacter(string[l]):
            l += 1
        elif specialCharacter(string[r]):
            r -= 1
        else:
            string = swap(string, l, r)
            l += 1
            r -= 1
    return string


def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


def specialCharacter(ch):
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        return 0
    elif '0' <= ch <= '9':
        return 1
    else:
        return 1


def main():
    testCases = int(input())
    while testCases > 0:
        inputs = []
        inputs.append(input().strip().split())
        arr = list(map(str, inputs[0]))
        print(reverseString(arr[0]))
        testCases = testCases - 1


if __name__ == "__main__":
    main()
