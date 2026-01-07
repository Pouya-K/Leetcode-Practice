from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            if midNum > target:
                right = mid
            else:
                left = mid
        
        return -1
            