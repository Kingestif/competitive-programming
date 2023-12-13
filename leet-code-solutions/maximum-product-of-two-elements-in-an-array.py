class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        print(nums, nums[-1]-1,nums[-2]-1)
        return (nums[-1] - 1) * (nums[-2] - 1)
