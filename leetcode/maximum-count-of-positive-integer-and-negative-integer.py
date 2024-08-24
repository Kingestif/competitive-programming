class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        lcount = 0
        rcount = 0
        for i in nums:
            if i < 0:
                lcount += 1
            elif i > 0:
                rcount += 1

        return max(rcount, lcount)