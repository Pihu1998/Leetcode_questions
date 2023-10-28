'''
Leetcode question: https://leetcode.com/problems/group-anagrams/
Level: Medium
Solution: Hash map
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Maintain a hashmap with key of type string and value of type "list of strings" so that 
        we can have multiple values for a particular key
        '''        
        seen ={}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:
                seen[sorted_word] = [word]    

        return seen.values()        
