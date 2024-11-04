class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        orisum = sum(rolls)
        totalcount = n + len(rolls)

        newsum = (mean * totalcount) - orisum
        val = newsum//n
        if val > 6 or val <= 0: 
            return []
        
        arr = [val] * n
        left = newsum - sum(arr)

        start = 0
        while left > 0:
            arr[start] += 1
            if arr[start] > 6 or val <= 0:
                return []
            start += 1
            left -= 1
        return arr



        



        
        
        
        