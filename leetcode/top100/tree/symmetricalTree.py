from Geeks.leetcode.tree_builder.tree_builder import Node, Tree


class Solution:
    def isSymmetric(self, root: Node) -> bool:
        return self.recSolve(root, root)

    def recSolve(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        c1 = t1.val == t2.val
        c2 = self.recSolve(t1.right, t2.left)
        c3 = self.recSolve(t1.left, t2.right)
        if c1 and c2 and c3:
            return True
        else:
            return False


tree = Tree()

arr = [1, 2, 2, 3, 4, 4, 3]
arr1 = [1, 2, 2, None, 3, None, 3]
for i in arr:
    tree.insert(i)

print(Solution().isSymmetric(tree.root))
