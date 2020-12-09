from typing import List


class Node:
    def __init__(self, val=0, left=None, right=None, level=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val:
                    if val < current.val:
                        if current.left:
                            current = current.left
                        else:
                            current.left = Node(val)
                            break
                    if val > current.val:
                        if current.right:
                            current = current.right
                        else:
                            current.right = Node(val)
                            break
                else:
                    break

    def treeBuilder2(self,node_list:List[int]) -> Node:
        root = Node(node_list[0])
        current_node_out = [root]
        ptr = 1

        while ptr < len(node_list):
            current_node_in = []
            for c in current_node_out:
                if node_list[ptr]:
                    new_node = Node(node_list[ptr])
                    c.left = new_node
                    current_node_in.append(new_node)
                ptr = ptr + 1
                if node_list[ptr]:
                    new_node = Node(node_list[ptr])
                    c.right = new_node
                    current_node_in.append(new_node)
                ptr = ptr + 1
            current_node_out = current_node_in

        self.root = root





    def bfs(self):  # Level order traversal
        if self.root.val is None:
            return
        queue = []
        out = []
        queue.append(self.root)
        while queue:

            current_node = queue.pop(0)
            out.append(current_node.val)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return out

    def inOrder(self): #stack DFS inorder
        if self.root.val is None:
            return
        stack = []
        current_node = self.root
        out = []
        while True:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            elif stack:
                current_node = stack.pop()
                out.append(current_node.val)
                current_node = current_node.right
            else:
                break

        return out



    def preOrder(self): #using stack
        if self.root is None:
            return
        stack = []
        stack.append(self.root)
        out = []
        while stack:
            current_node = stack.pop()
            out.append(current_node.val)

            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)

        return out



# tree = Tree()
# arr = [1,None,2,3]
# for i in arr:
#     tree.insert(i)
#
# print("Original Array", arr)
# print("BFS Array", tree.bfs())
# print("DFS InOrder", tree.inOrder())
# print("DFS PreOrder", tree.preOrder())
