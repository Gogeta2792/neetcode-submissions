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
            val = l1.val + l2.val + carry

            if val <= 9:
                curr.next = ListNode(val)
                carry = 0
            
            else:
                digit = val % 10
                curr.next = ListNode(digit)
                carry = 1
            
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
            
        if l1:
            if l1.val + carry <= 9:
                curr.next = ListNode(l1.val + carry)
                carry = 0
            else:
                while l1:
                    val = l1.val + carry

                    if val <= 9:
                        curr.next = ListNode(val)
                        carry = 0
                    
                    else:
                        digit = val % 10
                        curr.next = ListNode(digit)
                        carry = 1
                    
                    curr = curr.next
                    l1 = l1.next

        if l2:
            if l2.val + carry <= 9:
                curr.next = ListNode(l2.val + carry)
                carry = 0
            else:
                while l2:
                    val = l2.val + carry

                    if val <= 9:
                        curr.next = ListNode(val)
                        carry = 0
                    
                    else:
                        digit = val % 10
                        curr.next = ListNode(digit)
                        carry = 1
                    
                    curr = curr.next
                    l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
        

        return dummy.next