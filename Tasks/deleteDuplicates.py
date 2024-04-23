# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = head
        while head is not None and previous.next is not None:
            if previous.val == previous.next.val:
                previous.next =  previous.next.next
            else:
                previous = previous.next
        return head
        
