from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] > limit:
                left += 1
            else:
                left += 1
                right -= 1
            boats += 1
        
        return boats
    
sol = Solution()
print(sol.numRescueBoats([1,3,2,3,2], 3))