# Leetcode question: https://leetcode.com/problems/search-a-2d-matrix/
'''
Time complexity: O(n)
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:      
        for i in matrix:
            if target in i:
                return True
        return False
            
