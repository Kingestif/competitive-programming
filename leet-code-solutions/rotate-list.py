# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if it was a list, for rotating

        # for i in range(k):
        #     for j in range(len(head)):
        #         print((len(head)+j)%len(head))

        # O(N*2) TLE!!
        # to avoid TLE we need to modulus the K with the legnth of the list
        # calculate length
        if not head or not head.next:
            return head
        length = 0
        cal = head
        while cal:
            length += 1
            cal = cal.next
        k = k % length
       
        curr = head
        while k > 0:
            k -= 1
            start = head
            while start.next.next:
                start = start.next

            temp = start.next
            start.next = None
            temp.next = head
            head = temp

        return head



        