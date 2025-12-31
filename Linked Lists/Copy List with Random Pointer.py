from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        createdNodes = dict()
        createdNodes[None] = None

        curr = head
        while curr:
            if curr not in createdNodes:
                createdNodes[curr] = Node(0)
            if curr.next not in createdNodes:
                createdNodes[curr.next] = Node(0)
            if curr.random not in createdNodes:
                createdNodes[curr.random] = Node(0)
            
            createdNodes[curr].val = curr.val
            createdNodes[curr].next = createdNodes[curr.next]
            createdNodes[curr].random = createdNodes[curr.random]
            
            curr = curr.next
    
        return createdNodes[head]