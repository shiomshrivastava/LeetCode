# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # step 1: save next
            curr.next = prev        # step 2: reverse link
            prev = curr             # step 3: move prev
            curr = next_node        # step 4: move curr

        return prev