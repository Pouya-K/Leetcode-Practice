from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftLimit, rightLimit = 1, max(piles)
        result = rightLimit
            
        while leftLimit <= rightLimit:
            mid = (leftLimit + rightLimit) // 2
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                result = mid
                rightLimit = mid - 1
            else:
                leftLimit = mid + 1
        
        return result