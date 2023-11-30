class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0
        while i < len(arr):
            if(arr[i]==0):
                arr.insert(i,0)
                arr.pop()
                print(i,"ues")
                i+=2

            else:
                i+=1


