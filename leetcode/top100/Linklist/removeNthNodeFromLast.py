from Geeks.leetcode.top100.Linklist.linklistbuilder import LinkList

from Geeks.leetcode.top100.Linklist.linklistbuilder import ListNode

LL = LinkList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        l = 0
        current = head
        while current:
            l = l + 1
            current = current.next
        l = l - n
        current = dummy
        while l > 0:
            l = l - 1
            current = current.next
        current.next = current.next.next
        # LL.printLL()
        return dummy.next

    def removeNthFromEndOnePassAlgo(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        harePointer = dummy
        tortoisePointer = dummy
        for i in range(n + 2):
            harePointer = harePointer.next

        while harePointer:
            harePointer = harePointer.next
            tortoisePointer = tortoisePointer.next

        tortoisePointer.next = tortoisePointer.next.next
        LL.printLL()
        return dummy.next


def main():
    n = 2
    head = LL.head
    # Solution().removeNthFromEnd(head, n)
    Solution().removeNthFromEndOnePassAlgo(head, n)


if __name__ == "__main__":
    main()
