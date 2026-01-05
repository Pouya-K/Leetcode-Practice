from typing import List
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks).values()
        maxHeap = [-num for num in count]
        heapq.heapify(maxHeap)
        
        queue = deque()
        time = 0
        
        while maxHeap or queue:
            time += 1
            
            if not maxHeap:
                time = queue[0][1]
            else:
                task = -heapq.heappop(maxHeap) - 1
                if task != 0:
                    queue.append([-task, time + n])
            
            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time