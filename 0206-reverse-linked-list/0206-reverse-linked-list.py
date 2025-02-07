# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         prev = None  # Initialize previous pointer to None
         curr = head  # Start from the head of the list
    
         while curr:

            next_node = curr.next  # Store the next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr  # Move prev to the current node
            curr = next_node  # Move to the next node
    
         return prev  # New head of the reversed list