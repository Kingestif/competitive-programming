class Solution:
    def isBalanced(self, num: str) -> bool:
        sum1 = 0
        sum2 = 0
        for i in range(len(num)):
            if i%2 == 0:
                sum1 += int(num[i])
            else:
                sum2 += int(num[i])

        return sum1 == sum2

        


