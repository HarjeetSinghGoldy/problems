class TreeNode:
    def __inti__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2


def main():
    tree1 = [1, 3, 2, 5]
    tree2 = [2, 1, 3, None, 4, None, 7]

    print(Solution().mergeTree(tree1, tree2))


if __name__ == "__main__":
    main()
