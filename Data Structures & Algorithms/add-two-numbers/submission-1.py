# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 and l2:
            newVal = l1.val + l2.val + carry

            if newVal <= 9:
                curr.next = ListNode(newVal, None)
                carry = 0
            else:
                curr.next = ListNode(newVal % 10, None)
                carry = 1
            
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
            
        while l1:
            newVal = l1.val + carry

            if newVal <= 9:
                curr.next = ListNode(newVal, None)
                carry = 0
            else:
                curr.next = ListNode(newVal % 10, None)
                carry = 1
            
            l1 = l1.next
            curr = curr.next
        while l2:
            newVal = l2.val + carry

            if newVal <= 9:
                curr.next = ListNode(newVal, None)
                carry = 0
            else:
                curr.next = ListNode(newVal % 10, None)
                carry = 1
            
            l2 = l2.next
            curr = curr.next
        else:
            if carry:
                curr.next = ListNode(1, None)
            
        
        return dummy.next
