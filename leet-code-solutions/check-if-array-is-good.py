class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != len(set(nums)) + 1:
            return False

        if len(nums) != n+1:
            return False

        nums.sort()
        if nums[-1] and nums[-2] == n:
            return True
        
