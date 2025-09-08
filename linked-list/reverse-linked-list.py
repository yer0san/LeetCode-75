# difficulty : easy
# old one

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        cur_node = head
        prev_node = None
        next_node = head.next
        while next_node:
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            next_node = next_node.next
        cur_node.next = prev_node
        return cur_node
