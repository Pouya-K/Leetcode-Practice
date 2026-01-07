from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            curRow, curCol = mid // cols, mid % cols
            
            if matrix[curRow][curCol] == target:
                return True
            if matrix[curRow][curCol] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False