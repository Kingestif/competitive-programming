class Solution:
    def getSum(self, a: int, b: int) -> int:
        # REFER 1st SOLUTION TO GRASP BIT manipulation
        # lets make b the carry and a the sum
        mask = 0xffffffff

        while b != 0:
            temp = (a&b) << 1    #carry
            a = (a ^ b) &mask     #normal sum
            b = temp &mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a
        