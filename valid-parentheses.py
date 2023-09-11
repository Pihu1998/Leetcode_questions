'''
Leetcode question: https://leetcode.com/problems/valid-parentheses
Difficulty: Easy
O (n) complexity solution
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening tag to be closed
        stk = []

        # String to keep track of closing tag if it doesn't have a corresponding opening tag 
        # in stk
        close = "" 
        # Dict for closing tag with their opening tag for easy mapping
        known = {")":"(", "}": "{", "]": "["}
        for i in s:
            if i in known.values():
                stk.append(i)
            elif (len(stk) != 0) and (known[i] == stk[-1]):
                    stk.pop()
            else: #In the final case, the string definitely starts with closing tag
                close += i
           
        # Check if there's any opening tag still left to be closed  or if the string 
        # starts with closing tag, then it's not valid parenthesis

        if len(stk) != 0 or len(close) != 0:
            return False
        return True        
