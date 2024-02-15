class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        summ=sum(nums)
        for i in nums:
            if i < summ - i:
                return summ
            else:
                summ -= i
        return -1
