


# your task is to complete this function
# function should return an integer
def minDist(arr,l, x, y):
    # print(l, arr, x, y)
    prevIndex = 0
    min_dist = float('inf')
    for idx, val in enumerate(arr):
        if val == x or val == y:
            prevIndex = idx
            break
    for jdx in range(prevIndex + 1, l):
        if arr[jdx] == x or arr[jdx] == y:
            if arr[prevIndex] != arr[jdx] and (jdx - prevIndex) < min_dist:
                min_dist = jdx - prevIndex
                prevIndex = jdx
            else:
                prevIndex = jdx
    if  min_dist == float('inf'):
        return -1
    else:
        return min_dist



#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(minDist(arr, n, x, y))
# Contributed By: Shivam Gupta


# } Driver Code Ends