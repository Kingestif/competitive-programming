# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        ans = final
        check = True

        currentNode = head
        val = 0
        currentNode = currentNode.next
        while currentNode:
            if currentNode.val == 0:
                new = ListNode(val)
                ans.next = new
                ans = ans.next
                val = 0
            else:
                val += currentNode.val
            currentNode = currentNode.next
                
        final = final.next
        return final

                