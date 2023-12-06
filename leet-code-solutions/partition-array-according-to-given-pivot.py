class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        more=[]
        new=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            else:
                more.append(nums[i])

        length=len(less)

        for i in range(len(more)):
            if more[i] > pivot:
                less.append(more[i])
            else:
                less.insert(length,more[i])

        return less


        

            