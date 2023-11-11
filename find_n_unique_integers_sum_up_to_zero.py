'''
Leetcode problem: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
Time complexity: O(n/2)
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n%2 != 0:
            ans.append(0)
        nums = int(n/2)
        for i in range(1, nums+1):
            ans.append(i)
            ans.append(-i)

        return ans    
