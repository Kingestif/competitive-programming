# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans  = []
        for i in lists:
            curr = i
            while curr:
                ans.append(curr.val)
                curr = curr.next
                
        ans.sort()
        head = ListNode()
        curr = head
        for i in ans:
            head.next = ListNode(i)
            head = head.next


        return curr.next