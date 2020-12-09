# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Geeks.leetcode.top100.Linklist.linklistbuilder import ListNode, LinkList


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        result = self.iterativeSol(head, prev)
        # result = self.recSolve(head, prev)
        return result

    def recSolve(self, node, prev):
        if not node:
            return prev
        currentNode = node.next
        node.next = prev
        return self.recSolve(currentNode, node)

    def iterativeSol(self,head,prev):
        while head:
            currentNode = head
            head = head.next
            currentNode.next = prev
            prev = currentNode

        return prev





arr = [1, 2, 3, 4, 5]

ll = LinkList()

for i in range(len(arr)):
    ll.insert(arr[i])

print(Solution().reverseList(ll.head))
