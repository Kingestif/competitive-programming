class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max=float('-inf')
        for i in range(len(nums)-1):
            if i + nums[i] > max:
                max = i + nums[i]
            if max == i:
                return False
        return max >= len(nums) -1
            



        