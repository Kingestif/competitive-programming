# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Core: refer knowledge center
        if not head:
            return head

        # 1st create dummy node to point to the head
        start = ListNode()  ; start.next = head
        curr = head  ; prev = start
        while curr:
            if curr.next and (curr.next.val < curr.val):   #already sorted
                while prev.next and curr.next and (prev.next.val < curr.next.val):
                    prev = prev.next

                temp = prev.next
                prev.next = curr.next 
                curr.next = curr.next.next
                prev.next.next = temp
                prev = start    #make our prev start from begining for next iteration
            
            else:
                curr = curr.next

        return start.next
        
        