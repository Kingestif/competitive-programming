# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return True
        elif head.next==None:
            return True
        elif head.next.next==None:
            return head.val==head.next.val
        elif head.next.next.next==None:
            return head.val==head.next.next.val

        # length
        fast=head
        slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow
        slow=slow.next
        back=slow
        slow=slow.next

        # reverse
        # works but i cant delete the last node which is us unwanted
        while slow:
            newNode=ListNode(slow.val)
            mid.next=newNode
            newNode.next=back
            deleter=back
            back=newNode
            if slow.next==None:
                break

            slow.val=slow.next.val
            slow.next=slow.next.next    

        slow=head 
        
        # Comparing the first half and reversed half
        mid=mid.next
        while mid:
            if mid.val!=slow.val:
                return False

            if mid.next.next==None:
                break
            else:
                mid=mid.next
                slow=slow.next
        return True   
        
