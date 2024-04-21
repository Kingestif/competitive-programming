class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        summ = float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        if nums[i] + nums[j] + nums[k] < summ:
                            summ = nums[i] + nums[j] + nums[k]

        if summ == float('inf'):
            return -1
        return summ