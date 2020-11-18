from Geeks.leetcode.top100.Linklist.linklistbuilder import ListNode, LinkList


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        LLTemp = LinkList()
        LLTemp.insert(0)
        dummy = temp = LLTemp.head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        temp.next = l1 or l2

        print(LLTemp.printLL())
        return dummy.next


LL1 = LinkList()
LL2 = LinkList()
l1 = [1, 2, 4]
l2 = [1, 3, 4]

for i in range(len(l1)):
    LL1.insert(l1[i])

for i in range(len(l2)):
    LL2.insert(l2[i])

print(Solution().mergeTwoLists(LL1.head, LL2.head))
