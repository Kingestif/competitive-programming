class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(int)

        # this method hav memory limit
        # def dp(idx,sum1,sum2):
        #     if idx == len(nums): 
        #         if sum1 == sum2:
        #             return True
        #         else:
        #             return False

        #     if (idx,sum1,sum2) not in memo:
        #         memo[(idx,sum1,sum2)] = dp(idx+1,sum1+nums[idx],sum2) or dp(idx+1,sum1,sum2+nums[idx])
            
        #     return memo[(idx,sum1,sum2)]

        # return dp(0,0,0)

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

        