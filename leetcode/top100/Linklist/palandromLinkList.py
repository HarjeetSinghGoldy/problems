# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Geeks.leetcode.top100.Linklist.linklistbuilder import ListNode, LinkList


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:  #
        # find min of the linklist and reverese it
        fast = head
        slow = head
        reversedList = None

        while fast and fast.next:
            tmp = slow
            fast = fast.next.next
            slow = slow.next

            tmp.next = reversedList
            reversedList = tmp

        if fast is not None:
            slow = slow.next

        print(reversedList)

        while reversedList:
            if reversedList.val != slow.val:
                return False
            reversedList = reversedList.next
            slow = slow.next

        return reversedList is None


arr = [1, 2, 3, 2, 1]
arr = [1, 2, 3,3, 2, 1]
arr = [1,2]
ll = LinkList()

for i in range(len(arr)):
    ll.insert(arr[i])

print(Solution().isPalindrome(ll.head))
