# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        elif left == right:
            return head
        counter = 1
        currentNode = head
        forlatter = head
        
        before = head
        after = head
        length = 0
        while currentNode:
            length += 1
            if counter == left:
                reversed = ListNode(currentNode.val)
                newhead = reversed
                end = reversed
            elif counter <= right and counter > left:
                new = ListNode(currentNode.val)
                new.next = newhead
                newhead = new

            
            if counter + 1 == left:
                before = currentNode
            elif counter == right + 1:
                after = currentNode 

            currentNode = currentNode.next
            counter += 1

        print("before:",before.val,"after:",after.val,"reversed",newhead)
        # print("HEAD",head)
        # if left == 1:
        #     return newhead


        
        counter = 1
        iterator = head
        
        last = newhead
        counter = 1
        if left == 1 and right == length:
            return newhead

        elif left == 1:
            iter = newhead
            while iter.next:
                iter = iter.next

            iter.next = after
            iter = after

            return newhead

        elif right == length:
            before.next = last
            last = before
            return head

        before.next = last
        last = before
        
        iter = newhead
        while iter.next:
            iter = iter.next

        iter.next = after
        iter = after






        print("reversed",last)
        return head





            

                
        