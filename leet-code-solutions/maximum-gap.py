class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max=float('-inf')
        nums.sort()
        if len(nums)<=1:
            return 0

        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>max:
                max=nums[i]-nums[i-1]
        return max
        