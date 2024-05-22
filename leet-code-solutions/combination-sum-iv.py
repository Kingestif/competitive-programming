class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(target):
            for j in range(len(nums)):
                if i + nums[j] <= target:
                    dp[i+nums[j]] += dp[i]
        return dp[-1]
