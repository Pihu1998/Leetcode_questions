'''
Leetcode: https://leetcode.com/problems/longest-repeating-character-replacement
Solution: Sliding window
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        i= 0
        j = i+1
        arr=[]
        ch = s[i]
        arr.append(ch)
        while (j<len(s)):         
            if(s[j] != ch):
                if(k!=0):
                    arr.append(ch)
                    k-=1
                    count = max(len(arr), count)
                    j+=1
                else:
                    count = max(count, len(arr))
                    arr.clear()
                    i += 1
                    ch = s[i]
                    j = i+1
            else:
                arr.append(ch)                 
                count = max(len(arr), count)
                j+=1
          
        return count   
