class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        new=[]
        for i in range(1,len(nums)+1):
            prefix=set(nums[:i])
            suffix=set(nums[i:len(nums)+1])

            new.append(len(prefix)-len(suffix))

        return new
        