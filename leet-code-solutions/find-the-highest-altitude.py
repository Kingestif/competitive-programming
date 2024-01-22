class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new=[]
        total=0
        max=float('-inf')
        for i in range(len(gain)):
            if total>max:
                max=total
            new.append(total)
            total+=gain[i]
        new.append(total)
        if total > max:
            max=total
        return max

            
        