'''
Leetcode question: https://leetcode.com/problems/group-anagrams/
Level: Medium
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen ={}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:
                seen[sorted_word] = [word]    

        return seen.values()        
