'''
Leetcode problem: https://leetcode.com/problems/sign-of-the-product-of-an-array/
Time complexity: O(n)
'''

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for i in nums:
            if i > 0:
                prod*=1
            elif i<0:
                prod*=-1
            else:
                prod*=0

        return prod  
