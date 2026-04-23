# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        node=head
        n=0
        while node:
            n+=1
            node=node.next
        if k == n:
            return head.next
        i=0
        temp=head
        while i<n-k-1 :
            temp=temp.next
            i+=1
        temp.next=temp.next.next

        return head

        