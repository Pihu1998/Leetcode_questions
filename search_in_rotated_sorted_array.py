# Leetcode question: https://leetcode.com/problems/search-in-rotated-sorted-array/
'''
Time complexity: O(n)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            return nums.index(target)
