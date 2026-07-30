# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=dummy.next
        res=dummy
        while curr:
            if curr.val<x:
                res.next=ListNode(curr.val)
                res=res.next
            curr=curr.next
        curr=head
        while curr:
            if curr.val>=x:
                res.next=ListNode(curr.val)
                res=res.next
            curr=curr.next
        return dummy.next