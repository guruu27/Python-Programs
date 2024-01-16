class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
        dummy = temp = ListNode(0)
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                temp.next = l1
                l1= l1.next
            else:
                temp.next = l2
                l2= l2.next
            temp=temp.next
        temp.next = l1 or l2

        return dummy.next
