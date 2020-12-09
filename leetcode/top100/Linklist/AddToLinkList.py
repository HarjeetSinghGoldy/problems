from Geeks.leetcode.top100.Linklist.linklistbuilder import ListNode, LinkList


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = curNode = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            tempSum = v1 + v2 + carry
            carry, val = divmod(tempSum, 10)
            curNode.next = ListNode(val)
            curNode = curNode.next

        return res.next



arr1 = [2,4,3]
arr2 = [5,6,4]

llA = LinkList()
llB = LinkList()

for i in range(len(arr1)):
    llA.insert(arr1[i])

for i in range(len(arr2)):
    llB.insert(arr2[i])

print(Solution().addTwoNumbers(llA.head,llB.head))