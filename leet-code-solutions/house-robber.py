class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i == 0:  #we only have 1 house to rob
                return nums[0]
            if i == 1:  #we have 2 house, rob the none with max value
                return max(nums[0],nums[1])

            # return max(nums[i] + dp(i-2) , dp(i-1))
            #means if we chose
            if i not in memo:
                memo[i] = max(nums[i] + dp(i-2) , dp(i-1))
            return memo[i]

        return dp(len(nums) - 1)