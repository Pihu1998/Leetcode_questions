'''
Leetcode problem: https://leetcode.com/problems/search-a-2d-matrix
Time complexity: O(log(m * n))
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) -1
        size = len(matrix[0])

        while left <= right:
            mid = (left+right) // 2
            print("mid", mid)

            if matrix[mid][0] > target:
                right = mid-1
                continue
            elif matrix[mid][-1] < target:
                left = mid+1
                continue
            else:
                l = 0
                r = size-1
                while (l <= r):
                    m = (l+r) // 2
                    print("m", m)
                    if matrix[mid][m] > target:
                        r = m-1
                    elif matrix[mid][m] < target:
                        l = m+1
                    else:
                        return True
            return False
