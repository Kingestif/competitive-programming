# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = l1  ;   iter2 = l2  
        rem = 0
        num = str(l1.val + l2.val)
        if len(num) == 2:   #means we have remainder
            l3 = ListNode(int(num[1]))
            rem = int(num[0])
        else:
            l3 = ListNode(int(num[0]))

        l1 = l1.next    ;   l2 = l2.next
        iter3 = l3

        # this works but if either one of them finish before the other we need ANOTHER loops to handle that
        while l1 and l2:
            num = str(l1.val + l2.val + rem)
            if len(num) == 2:
                temp = ListNode(int(num[1]))
                rem = int(num[0])
                iter3.next = temp
                iter3 = iter3.next

            else:
                temp = ListNode(int(num[0]))
                iter3.next = temp
                iter3 = iter3.next
                rem = 0
            l1 = l1.next    ;   l2 = l2.next

        print("yes1",rem)

        while l1:
            num = str(l1.val + rem)
            if len(num) == 2:
                temp = ListNode(int(num[1]))
                rem = int(num[0])
                iter3.next = temp
                iter3 = iter3.next
            else:
                temp = ListNode(int(num[0]))
                iter3.next = temp
                iter3 = iter3.next
                rem = 0
            l1 = l1.next
        print("yes2",rem)

        while l2:
            num = str(l2.val + rem)
            if len(num) == 2:
                temp = ListNode(int(num[1]))
                rem = int(num[0])
                iter3.next = temp
                iter3 = iter3.next
            else:
                temp = ListNode(int(num[0]))
                iter3.next = temp
                iter3 = iter3.next
                rem = 0
            l2 = l2.next
                
        if rem > 0:
            temp = ListNode(rem)
            iter3.next = temp
            iter3 = iter3.next
        return l3
        
      

# carry = num // 10
# digit = num % 10
# temp = ListNode(digit)
# iter3.next = temp
# iter3 = iter3.next
# rem = carry
