# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        new_head = stack.pop() #reference to head
        new_curr = new_head
        while stack:
            new_curr.next = stack.pop()
            new_curr = new_curr.next

        new_curr.next = None #hence new_curr is reference to tail

        return new_head