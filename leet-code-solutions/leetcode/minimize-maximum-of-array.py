import math
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # the upper give to lower then the lower give it to lower eyale eyale optimize mareg do for 2 3 7
        max=nums[0]
        total=nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            if math.ceil(total / (i+1)) > max:
                max = math.ceil(total / (i+1))
        return max
