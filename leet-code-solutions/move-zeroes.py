class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start=0
        # end=1
        # while end<len(nums):
        #     if nums[start]==0 and nums[end]==0:
        #         end+=1
        #     elif nums[start]==0 and nums[end]!=0:
        #         nums[start],nums[end]=nums[end],nums[start]
        #         end+=1 ; start+=1
        #     else:
        #         end+=1 ; start+=1

        # return nums

        # method 2 just put the non zero to index 0
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
        return nums


        