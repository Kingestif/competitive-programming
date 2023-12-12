import math
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit=(len(arr)*25)//100

        limit+=1

        for i in range(len(arr)):
            if arr.count(arr[i])>=limit:
                return arr[i]



