# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # USING DICTIONARY

        # map={}
        # currentNode=head
        # while currentNode:
        #     if currentNode in map:
        #         return True
        #     map[currentNode]=1
        #     currentNode=currentNode.next
        # return False

        # USING 2 POINTERS
        if head==None:
            return False
        # elif head.next==None:
        #     return False
        # elif head.next.next==None:
        #     return False

        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next ; fast=fast.next.next
            if slow==fast:
                return True
        return False

        