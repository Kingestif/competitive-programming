class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = list(str(n))
        x = 0
        count = 0
        for i in range(len(n)):
            if x == 0:
                count += int(n[i])
                x = 1
            else:
                count -= int(n[i])
                x = 0
        return count
