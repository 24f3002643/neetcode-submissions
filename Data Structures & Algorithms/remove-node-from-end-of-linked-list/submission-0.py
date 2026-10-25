# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        length = 0
        temp = dummy
        temp = temp.next
        while temp:
            length += 1
            temp = temp.next

        temp = dummy
        for i in range(length-n):
            temp = temp.next
        
        temp.next = temp.next.next

        return dummy.next
        

        