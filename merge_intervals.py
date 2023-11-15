'''
Leetcode question: https://leetcode.com/problems/merge-intervals/
Time Complexity: O(n)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output =[intervals[0]]
        for i, j in intervals[1:]:
            lastEnd = output[-1][1]
            if i <= lastEnd:
                output[-1][1] = max(lastEnd, j)
            else:
                output.append([i,j])    

        return output   
