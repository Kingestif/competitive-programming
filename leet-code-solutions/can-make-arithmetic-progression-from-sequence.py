class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) == 1 or len(arr) ==0:
            return True
        
        count=abs(arr[0]-arr[1])
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) != count:
                return False
        return True

