# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        iterator = newNode
        ls = []

        while head:
            ls.append(head.val)
            head = head.next

        print(ls)

        for i in range(len(ls)-1):
            temp = ListNode(ls[i])
            iterator.next = temp
            iterator = iterator.next
            GCD = math.gcd(ls[i], ls[i+1])
            temp = ListNode(GCD)
            iterator.next = temp
            iterator = iterator.next

        temp = ListNode(ls[-1])
        iterator.next = temp
        iterator = iterator.next



        return newNode.next


        