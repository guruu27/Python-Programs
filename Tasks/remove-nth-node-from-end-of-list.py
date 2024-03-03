# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self, head: Optional[ListNode]):
        len = 0
        temp = head
        while temp is not None:
            temp = temp.next
            len += 1
        return len
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.len(head)
        
        if l <= n:
            return head.next
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        p=0
        dummy = head
        while  p < l - n:
            temp = temp.next
            p+=1
        temp.next = temp.next.next
        return dummy
            
