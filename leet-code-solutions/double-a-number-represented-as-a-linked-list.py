# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(100000)
        curr = head
        val = ""
        while curr:
            val += str(curr.val)
            curr = curr.next

        val = str(int(val) * 2)

        i = 0
        new = ListNode(int(val[0]))
        curr = new

        for i in range(1,len(val)):
            temp = ListNode(int(val[i])) 
            curr.next = temp
            curr = curr.next

        return new



