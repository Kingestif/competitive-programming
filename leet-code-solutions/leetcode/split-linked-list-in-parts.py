# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []    ; length = 0    ; add = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        base , extra = length // k , length % k

        curr = head
        
        for i in range(k):
            ans.append(curr)

            if extra > 0: add = 1   
            else: add = 0

            # this loop is to cut out the links since that is what we return
            for i in range(base -1 + add): #if we have extra we need to include that
                if not curr:
                    break
                curr = curr.next

            extra -= 1

            # move the next pointer to None to officially cut out the link
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp # then make current, the head of the next list

        return ans
            



        



