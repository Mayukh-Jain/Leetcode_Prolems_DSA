# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        less=dummy
        mh=ListNode(0)
        more=mh
        while head:
            if head.val<x:
                less.next=head
                less=less.next
            else:
                more.next=head
                more=more.next
            head=head.next
        less.next=mh.next
        more.next=None
        return dummy.next