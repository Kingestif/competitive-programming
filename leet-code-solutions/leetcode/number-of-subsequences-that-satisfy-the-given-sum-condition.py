class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        for i in range(len(nums)):
            if target - nums[i] >= nums[i]:
                index = bisect_right(nums,target - nums[i]) 
                total += 2 ** (index - i - 1) 

        return total % (10**9 + 7)

        





            