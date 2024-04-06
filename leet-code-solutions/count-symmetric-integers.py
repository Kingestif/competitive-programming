class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            s = list(map(int,str(i)))
            if len(s) % 2 == 0:
                if sum(s[:len(s)//2]) == sum(s[len(s)//2:]):
                    count += 1
        return count

