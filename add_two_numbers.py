'''
Leetcode question: https://leetcode.com/problems/add-two-numbers/
Solution language: Python 3
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Idea is to traverse each linked list and append the numbers into a string for each linked list.  
        l1_number = ""
        l2_number = ""

        while(l1 is not None):        
            l1_number += str(l1.val)
            l1 = l1.next
 
        while(l2 is not None):                  
            l2_number += str(l2.val)
            l2 = l2.next    

        l3_number = int(l1_number[::-1]) + int(l2_number[::-1])
   
        dummyhead = ListNode(0)
        l3 = dummyhead
        for c in map(int, str(l3_number)[::-1]):
            newNode = ListNode(int(c))
            l3.next = newNode
            l3 = l3.next

        return dummyhead.next
