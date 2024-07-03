class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # easy 
        nums.sort()
        if len(nums) <= 4:
            return 0
        ans1 = nums[-1] - nums[3]
        ans2 = nums[len(nums)-4] - nums[0]
        ans3 = nums[len(nums)-3] - nums[1]
        ans4 = nums[len(nums)-2] - nums[2]
        return min(ans1,ans2,ans3,ans4)

        
                

        