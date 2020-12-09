from typing import List

from Geeks.Recursions_And_DP.Tree.tree_builder import TreeNode
from Geeks.leetcode.tree_builder.tree_builder import Tree, Node


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        return root


arr = [3, 9, 20, None, None, 15, 7]
tree = Tree()

tree.treeBuilder2(arr)

print(Solution().levelOrder(tree.root))
