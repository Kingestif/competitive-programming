class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(int)
        if sum(nums) % 2 != 0:  #means we can't divide it equally
            return False

        def dp(idx,val):
            if idx == len(nums) or val < 0:
                return False

            if val == 0:
                return True

            if (idx,val) not in memo:
                memo[idx,val] = dp(idx+1, val - nums[idx]) or dp(idx+1,val)

            return memo[idx,val]

        return dp(0,sum(nums)//2)

        