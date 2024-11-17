class Solution(object):
    def searchInsert(self, nums, target):
        start=0
        end=len(nums)-1
        mid=(start+end)//2

        while(start<=end):
        
            if target<nums[mid] and target>nums[mid-1]: 
                return mid
            if target<nums[0]:
                return 0
                

            if target>nums[len(nums)-1]:
                return len(nums)
                

            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                end=mid-1
                mid=(start+end)//2
            elif target>nums[mid]:
                start=mid+1
                mid=(start+end)//2









        