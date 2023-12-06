class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max=0
        for i in range(len(nums)-2):
            sum=nums[i]+nums[i+1]+nums[i+2]
            if(nums[i]+nums[i+1]>nums[i+2] and sum>max):
                max=sum

        return max



