# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        tail=head
        count=1
        while tail.next!=None:
            count+=1
            tail=tail.next
        k=k%count
        if k==0:
            return head
        tail2=head
        for i in range(count-k-1):
            tail2=tail2.next
        temp=tail2.next
        tail2.next=None
        tail.next=head
        return temp
        #can be faster
