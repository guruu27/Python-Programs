# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        ll = dummy = ListNode()
        carry = 0
        while n1 or n2 or carry:
            res = carry
            if n1:
                res+=n1.val
                n1 = n1.next
            if n2:
                res+=n2.val
                n2 = n2.next
            unit = int(res%10)
            ll.next = ListNode(unit)
            ll = ll.next
            carry = res//10
        return dummy.next
        
