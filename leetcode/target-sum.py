class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        memo = defaultdict(int)

        def dp(idx,summ):
            nonlocal count
            if idx >= len(nums):    
                if summ == target:
                    return 1
                return 0

            if (idx,summ) not in memo:
                memo[(idx,summ)] = dp(idx+1,summ - nums[idx] -nums[idx]) + dp(idx+1,summ)
            return memo[(idx,summ)]

        return dp(0,sum(nums))