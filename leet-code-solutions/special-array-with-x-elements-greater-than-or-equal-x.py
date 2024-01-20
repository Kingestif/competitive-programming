class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            num=0
            for j in range(len(nums)):
                if nums[j] >= i:
                    num+=1
            if i==num:
                return i
        return -1
        