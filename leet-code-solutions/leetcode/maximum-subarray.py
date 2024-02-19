class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        total=float('-inf')
        for i in range(0,len(nums)):
            if(nums[i]>sum and sum<0):
                sum=0
                sum=sum+nums[i]
            else:
                sum=sum+nums[i]

            if(sum>total):
                total=sum

        return total