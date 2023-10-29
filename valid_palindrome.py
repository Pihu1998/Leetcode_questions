'''
Leetcode question: https://leetcode.com/problems/valid-palindrome/
Solution: Regex and string reverse
Difficulty level: Easy
'''

class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:    
        pattern = "[^0-9a-zA-Z]+"
        phrase = re.sub(pattern, '', s)
        if phrase.lower() == phrase[::-1].lower():
            return True
        else:
            return False    
