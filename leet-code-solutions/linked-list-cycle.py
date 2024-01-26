# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map={}
        currentNode=head
        while currentNode:
            if currentNode in map:
                return True
            map[currentNode]=1
            currentNode=currentNode.next
        return False
        