class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        while n >= 0:
            count = 0
            temp = n
            while temp > 0:
                if temp%2 == 1:
                    count += 1
                temp//=2


            ans.append(count)
            n -= 1
        ans.reverse()
        return ans
            
