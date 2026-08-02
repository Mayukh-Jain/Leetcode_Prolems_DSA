class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head

        curr = head
        prev = None
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        if head:
            head.next = self.reverseKGroup(curr, k)

        return prev