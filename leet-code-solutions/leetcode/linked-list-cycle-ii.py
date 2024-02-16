# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        slow=head ; fast=head  ; checkmap={} ; isCycle=False
        map={slow:0}

        # to find if odd or even
        checker=head    ; counter=0
        while checker:
            if checker not in checkmap:
                checkmap[checker]=1
            else:
                isCycle=True
                break
            checker=checker.next
            counter+=1
        print("count: ",counter)

        if not isCycle:
            return None
            
        num=1
        while slow.next and fast.next.next:
            slow=slow.next
            prev=fast.next  #not updating
            fast=fast.next.next
            if slow not in map:
                map[slow]=num
                num+=1

            if fast in map:
                if counter % 2 != 0:
                    return prev
                return fast

        