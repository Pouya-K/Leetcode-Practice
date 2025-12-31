from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, ahead = head, head
        prev = None

        for i in range(n):
            ahead = ahead.next
        
        while ahead:
            prev = curr
            curr = curr.next
            ahead = ahead.next
        
        if not prev:
            return head.next

        prev.next = curr.next
        return head