# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        p=ans=ListNode(0)
        p.next=head
        if not head:
            return

        while p:
            while p.next and p.next.val==val:
                p.next=p.next.next
            p=p.next

        return ans.next
