# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        map={}
        currentNode = headA
        while currentNode:
            if currentNode not in map:
                map[currentNode] = 1
            currentNode = currentNode.next
        currentNodeB = headB

        while currentNodeB:
            if currentNodeB in map:
                return currentNodeB
            
            currentNodeB = currentNodeB.next

        

