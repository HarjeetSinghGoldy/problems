import sys
from collections import deque

sys.setrecursionlimit(50000)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -sys.maxsize

        def helperRecusive(node):
            if node is None:
                return 0
            leftDiameter = helperRecusive(node.left)
            rightDiameter = helperRecusive(node.right)

            temp = max(max(leftDiameter, rightDiameter) + node.val, node.val)
            ans = max(temp, leftDiameter + rightDiameter + node.val)
            self.res = max(self.res, ans)
            return temp

        helperRecusive(root)
        return self.res


def treeBuilder(arr):
    # cornerCase
    if len(arr) == 0 or arr[0] == "N":
        return None

    root = TreeNode(arr[0])
    size = 0
    q = deque()

    q.append(root)
    size = size + 1

    i = 1
    while size > 0 and i < len(arr):
        currNode = q[0]
        q.popleft()
        size = size - 1

        # left side
        currVal = arr[i]
        if currVal != "N":
            currNode.left = TreeNode(currVal)
            q.append(currNode.left)
            size = size + 1
        # right side
        i = i + 1
        if i >= len(arr):
            break

        currVal = arr[i]

        if currVal != "N":
            currNode.right = TreeNode(currVal)

            q.append(currNode.right)
            size = size + 1
        i = i + 1

    return root


def main():
    arr = list(map(int, input().strip().split()))
    root = treeBuilder(arr)
    print(Solution().maxPathSum(root))


if __name__ == "__main__":
    main()
