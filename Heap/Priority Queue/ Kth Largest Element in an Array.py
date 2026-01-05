from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        
        for num in nums:
            if num not in minHeap:
                heapq.heappush(minHeap, -num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return -minHeap[k-1]