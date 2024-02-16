# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter=0
        currentNode=head
        if head==None:  #if no element
            return head
        if head.next==None: #if 1 element
            return head

        while currentNode.next!=None:
            # for appending to front
            newnode=ListNode(currentNode.next.val)     
            newnode.next=head
            head=newnode

            # the Core code: it iterates over by breaking the links
            currentNode.next=currentNode.next.next
        return head