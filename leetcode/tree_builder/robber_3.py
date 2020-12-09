# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Geeks.Recursions_And_DP.Tree.tree_builder import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        result = [0, 0]
        self.recSolve(root, result)
        return max(result[0], result[1])

    def recSolve(self, node, result):
        if not node:
            return [0, 0]
        else:
            leftTree = self.recSolve(node.left, result)
            rightTree = self.recSolve(node.right, result)
            # include node
            result[0] = node.val + leftTree[1] + rightTree[1]
            # not include
            result[1] = max(leftTree[0], leftTree[1]) + max(rightTree[0], rightTree[1])

            return result
