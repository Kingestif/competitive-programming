# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        elif head.next==None:
            return head
        currentNode=head
        while currentNode.next:
            if currentNode.val==currentNode.next.val:
                currentNode.next=currentNode.next.next
            else:
                currentNode=currentNode.next
        return head