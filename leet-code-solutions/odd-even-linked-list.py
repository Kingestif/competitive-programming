# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None: #if empty
            return head
        elif head.next==None:  #if only one value
            return head
        elif head.next.next==None: #if only 2 values
            return head
            
        endNode=head
        length=1
        while endNode.next!=None:
            endNode=endNode.next
            length+=1
        print(endNode.val,length)

        counter=1
        currentNode=head
        while counter < length:
            if counter%2!=0:
                temp=currentNode.next
                currentNode.next=currentNode.next.next
                endNode.next=temp
                endNode=temp
                currentNode=currentNode.next
                temp.next=None
                counter+=2
        return head

        


        
        