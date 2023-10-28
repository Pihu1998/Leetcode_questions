'''
Leetcode question: https://leetcode.com/problems/contains-duplicate/
Solution: Python
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if sorted(nums) != sorted(list(set(nums))):
            return True
        else:
            return False   
