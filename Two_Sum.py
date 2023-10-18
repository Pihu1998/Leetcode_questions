'''
Array problem
Complexity: O(n)
Solution: Using hash table
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Defined hash table to keep track of all seen elements with their indices'''
        seen = {}
        for i in range(len(nums)):
            
            '''Using diff with target approach to find the second number in the array'''
            diff = target - nums[i]

            '''Return if the second number is seen'''
            if diff in seen:
                return [seen[diff], i]
            else:
                '''Else add what we saw'''
                seen[nums[i]] = i    
