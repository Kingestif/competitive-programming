# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            head=None
            return
        start=0 ; end=0
        currentNode=head

        while end < n-1:
            end+=1
            currentNode=currentNode.next

        end-=1
        nthNode=head
        prev=head

        while currentNode.next!=None:
            end+=1
            currentNode=currentNode.next

            if currentNode.next!=None:
                prev=prev.next
            
            nthNode=nthNode.next
        print("nth Node: ",nthNode.val)
        print("prev Node: ",prev.val)

        

        # to delete it
        if nthNode.next==None:  #we need previous node for this case
            prev.next=None
        else:   #the below 2 codes first refer to Q.237
            nthNode.val=nthNode.next.val
            nthNode.next=nthNode.next.next
            
        return head
        