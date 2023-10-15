'''
https://leetcode.com/problems/reverse-integer/
Time complexity: O(1)
Space complexity: O(1)
'''

class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1
        x = str(abs(x))
        x = int(x[::-1])
        return flag*x if x<=(2**31) else 0
