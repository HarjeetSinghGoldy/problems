# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Geeks.Recursions_And_DP.Tree.diameter_of_b_tree import TreeNode
from Geeks.leetcode.tree_builder.tree_builder import Tree


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        result  = self.recSolve(root)
        return result

    def recSolve(self,root):
        if not root:
            return None

        right = self.recSolve(root.right)
        left = self.recSolve(root.left)

        root.left = right
        root.right = left

        return root

t = Tree()

arr = [1,2,3,4,5,6,8]

for i in range(len(arr)):
    t.insert(arr[i])

print(Solution().invertTree(t.root))