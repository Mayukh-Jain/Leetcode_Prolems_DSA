# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dm=ListNode(0)
        curr=dm
        carry=0

        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            s=val1+val2+carry
            carry=s//10
            nval=s%10
            curr.next=ListNode(nval)
            curr=curr.next
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return dm.next