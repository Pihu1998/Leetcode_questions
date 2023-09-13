'''
Leetcode: https://leetcode.com/problems/linked-list-cycle
Algorithm used: Hare and Tortoise/ Floys's cycle-finding algorithm
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None):
            return False
        
        # l = []
        visited_nodes = set()
        while(head and head.next):
            if(head in visited_nodes):
                return True
            # l.append(head.val)   
            visited_nodes.add(head)
            head = head.next 
        return False 
