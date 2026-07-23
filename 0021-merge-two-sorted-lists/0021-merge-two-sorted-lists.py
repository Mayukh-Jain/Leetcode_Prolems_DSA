# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy

        while l1 and l2:
            v1=l1.val
            v2=l2.val
            if v1<=v2:
                curr.next=l1
                curr=curr.next
                l1=l1.next
            else:
                curr.next=l2
                curr=curr.next
                l2=l2.next
        p=l1 or l2
        while p:
            curr.next=p
            curr=curr.next
            p=p.next
        return dummy.next