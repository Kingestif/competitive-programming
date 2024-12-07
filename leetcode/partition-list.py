# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None:
            return head
        elif head.next==None:
            return head

        currentNode=head
        counter=0 ; checkl=False ; checkr=False
        while currentNode:
            if not checkl and currentNode.val < x:
                left=ListNode(currentNode.val)
                itlef=left
                checkl=True
            elif not checkr and currentNode.val >= x:
                right=ListNode(currentNode.val)
                itrig=right
                checkr=True
            else:
                if currentNode.val < x:
                    temp=ListNode(currentNode.val)
                    itlef.next=temp
                    itlef=itlef.next
                elif currentNode.val >= x:
                    temp=ListNode(currentNode.val)
                    itrig.next=temp
                    itrig=itrig.next
            currentNode=currentNode.next
        if not checkr:
            return left
        elif not checkl:
            return right
        itlef.next=right
        return left
            



        
        