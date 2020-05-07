def getCommon(n1, n2, n3, arr1, arr2, arr3):
    i = j = k = 0
    resDict = {}
    while i < n1 and j < n2 and k < n3:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        elif arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            if i not in resDict:
                resDict[arr1[i]] = 1
                print(arr1[i], end=" ")
            i += 1
            j += 1
            k += 1
        else:
            k += 1

    if not resDict:
        print(-1, end=" ")
    print()


def test():
    tcases = int(input())
    for t in range(tcases):
        n1, n2, n3 = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        arr3 = list(map(int, input().strip().split()))
        getCommon(n1, n2, n3, arr1, arr2, arr3)
if __name__ == "__main__":
    test()
