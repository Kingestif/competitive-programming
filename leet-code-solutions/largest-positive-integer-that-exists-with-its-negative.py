from collections import Counter
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums.sort(reverse = True)
        for i in nums:
            if -1*i in count:
                return i
        return -1
