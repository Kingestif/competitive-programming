class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total=0
        first=0
        for i in range(1,len(nums)):
            if nums[first]!=nums[i]:
                total+=i
                nums[first]=nums[i]

        return total


