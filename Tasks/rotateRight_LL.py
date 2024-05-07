# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        curr = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1
        temp.next = head
        k = k%length
        temp = head
        for _ in range(length-1-k):
            temp = temp.next
        res = temp.next
        temp.next = None
        return res
