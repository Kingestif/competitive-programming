class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countSetBit(num):
            return bin(num).count('1')


        #Bubble sort
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if countSetBit(nums[j]) == countSetBit(nums[j+1]) and nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


        return nums == sorted(nums)



