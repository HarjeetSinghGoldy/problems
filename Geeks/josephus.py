# {
# Driver Code Starts
import math


# } Driver Code Ends

# Complete this function
def josephus(n, k):
    # Your code here
    print("n", n)
    if n == 1:
        return n
    return (josephus(n - 1, k) + k)


# {
# Driver Code Starts.

def main():
    T = int(input())

    while (T > 0):
        nk = [int(x) for x in input().strip().split()]
        n = nk[0]
        k = nk[1]
        print(josephus(n, k))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
