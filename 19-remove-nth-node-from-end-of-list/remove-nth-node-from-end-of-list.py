# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=ListNode(0)
        p.next=head
        first=p
        second=p

        for _ in range(n+1):
            first=first.next
        
        while first is not None:
            first=first.next
            second=second.next

        second.next=second.next.next
        return p.next

            