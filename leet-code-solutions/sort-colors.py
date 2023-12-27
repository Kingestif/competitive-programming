class Solution(object):
    def sortColors(self, nums):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(i!=j and nums[i]<nums[j]):
                    (nums[i],nums[j])=(nums[j],nums[i])
        return nums
        