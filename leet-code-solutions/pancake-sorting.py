from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr==sorted(arr):
            return []
        # how to sort using pancake method
        flips=[]
        for i in range(len(arr),0,-1):
            max=float('-inf')
            imax=0
            for j in range(i):
                if arr[j]>max:
                    max=arr[j]
                    imax=j

            arr[0:imax+1] = arr[0:imax+1][::-1]
            flips.append(imax + 1)
            arr[0:i] = arr[0:i][::-1]
            flips.append(i)

        return flips




        