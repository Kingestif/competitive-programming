# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        elif list2==None:
            return list1
            
        first=list1 ; second=list2
        counter=0
        while first and second:
            if counter==0:
                counter+=1
                if first.val<second.val:
                    newnode=ListNode(first.val)
                    traversal=newnode
                    first=first.next
                else:
                    newnode=ListNode(second.val)
                    traversal=newnode
                    second=second.next
            elif first.val < second.val:
                traversal.next=first
                first=first.next
                traversal=traversal.next
            else:
                traversal.next=second
                traversal=traversal.next
                second=second.next
        if not first and not second:
            return newnode
        elif not first:
            while second:
                traversal.next=second
                traversal=traversal.next
                second=second.next
            return newnode
        else:
            while first:
                traversal.next=first
                traversal=traversal.next
                first=first.next
            return newnode
        

        