class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        start = 0 ; end = len(nums) -1
        s = set()
        for i in range(len(nums)//2):
            s.add((nums[i] + nums[end])/2)
            end -= 1

        return len(s)