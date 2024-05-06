class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # val = left
        # while left <= right:
        #     if not val:
        #         break

        #     val = val & left
        #     left += 1

        # return val
        
        # refer codeTree 
        # if all bit numbers get same when we rightshift them it means ther is not flip on the bits(no 0's')
        count = 0
        while left != right:
            left = left >> 1   ;   right = right >> 1
            count += 1


        if left == 0:
            return 0

        # if they are the same it means it can never be 0 so add back the 0's you remove by leftshift
        while count:
            left = left << 1
            count -= 1

        return left



