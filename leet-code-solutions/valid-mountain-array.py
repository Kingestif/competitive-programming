class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up=True
        if len(arr)==1:
            return False
            
        for i in range(len(arr)-1):
            if i==0 and arr[i]>arr[i+1]:
                return False
            if up==True:
                if arr[i]==arr[i+1]:
                    return False
                elif arr[i]>arr[i+1]:
                    up=False

            else:
                if arr[i]<=arr[i+1]:
                    return False

        if up!=False:   #if its only increasing
            return False

        return True


            
        