# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        newNode = ListNode()
        iterator = newNode
        first = list1   ;   second = list2

        i = 0
        while first:
            if i == a:
                x = b - a + 1
                while second:
                    iterator.next = second
                    iterator = iterator.next
                    second = second.next

                while x > 0:
                    first = first.next
                    x -= 1
                i += 1
            else:
                iterator.next = first
                iterator = iterator.next
                first = first.next
            i += 1

        return newNode.next



