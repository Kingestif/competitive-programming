class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        # more optimized
        n=len(nums)
        cumulative_sum = (n * (n + 1)) // 2
        return cumulative_sum - sum(nums)
        
        