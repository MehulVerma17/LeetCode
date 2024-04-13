# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        c=0
        while a!=None:
            c+=1
            a=a.next
        mid=c//2
        if mid==0:
            del head
        else:   
            p=head
            for i in range(0,mid-1):
                p=p.next
            temp=p.next
            p.next=temp.next
            del(temp)
            return head