# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start from Back
        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next

        new = ListNode(ans[-1])
        iter = new
        prevLarge = ans[-1]
        for i in range(len(ans)-2,-1,-1):
            if ans[i] < prevLarge:
                continue
            prevLarge = ans[i]
            iter.next = ListNode(ans[i])
            iter = iter.next

        # now just reverse the linked list
        rev = []
        curr = new
        while curr:
            rev.append(curr.val)
            curr = curr.next
        
        rev.reverse()
        rever = ListNode(rev[0])
        iter = rever
        for i in range(1,len(rev)):
            iter.next = ListNode(rev[i])
            iter = iter.next
        return rever

            






