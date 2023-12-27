class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr1=[None]*len(nums)
        for i in range(0,len(nums)):
            sum=0
            for j in range(0,len(nums)):
                if(i!=j and nums[j]<nums[i]):
                    sum+=1

            arr1[i]=sum
        return arr1

