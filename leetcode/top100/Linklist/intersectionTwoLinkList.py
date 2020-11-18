from Geeks.leetcode.top100.Linklist.linklistbuilder import LinkList



class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB :
            return None
        p = headA
        q = headB

        while p and q and p != q:
            p = p.next
            q = q.next

            if p == q:
                print(p, q)
                return q

            if not p:
                p = headB

            if not q:
                q = headA
        return p


ll1 = LinkList()
ll2 = LinkList()
arr1 =[4,1,8,4,5]
arr2 =[5,6,1,8,4,5]
intersectionPoint = 8


for i in range(len(arr1)):
    ll1.insert((arr1[i]))
for i in range(len(arr2)):
    ll2.insert((arr2[i]))

lenLL1 = 0
curA = ll1.head
lenLL2 = 0
curB = ll2.head
while curA:
    curA = curA.next
    lenLL1 = lenLL1 + 1
while curB:
    curB= curB.next
    lenLL2 = lenLL2 + 1

curA = ll1.head
curB = ll2.head

for i in range(2-1):
    curA = curA.next

for i in range(3):
    curB = curB.next

curA.next = curB


print(Solution().getIntersectionNode(ll1.head,ll2.head))