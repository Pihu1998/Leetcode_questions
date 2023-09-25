'''
Leetcode question: https://leetcode.com/problems/find-the-difference/
Time complexity: O(n)
space complexity: O(n)
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_count = {x:s.count(x) for x in set(s)}
        
        for i in t:
            if i not in s or (i in s and list_count[i] < t.count(i)):
                return i
