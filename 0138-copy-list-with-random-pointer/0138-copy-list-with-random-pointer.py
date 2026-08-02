"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        curr=head        
        while curr:
            nxt=curr.next
            curr.next=Node(curr.val,nxt)
            curr=nxt
        
        curr=head
        while curr:
            curr.next.random=curr.random.next if curr.random else None
            curr=curr.next.next

        curr=head
        h2=head.next
        while curr:
            copy=curr.next
            curr.next=copy.next
            if copy.next: 
                copy.next=copy.next.next
            curr=curr.next
        
        return h2