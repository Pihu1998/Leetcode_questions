# Leetcode question: 	1. https://leetcode.com/problems/longest-substring-without-repeating-characters

'''
Solution:
Technique: Sliding Window
Complexity: O(n)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        seen = {}
        left = 0
        longest=0
        for right in range(len(s)):
            if s[right] in seen and left<=seen[s[right]]:
                left = seen[s[right]] + 1
                seen[s[right]] = right
            else:
                seen[s[right]] = right
                longest = max(longest, right-left +1) 
        return longest        

