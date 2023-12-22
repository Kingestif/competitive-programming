class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small=float('inf') ; small2=float('inf')
        for i in range(len(nums)):
            if nums[i]<=small:
                small=nums[i]
            elif nums[i]<=small2:
                small2=nums[i]
            else:
                return True
        else:
            return False



            
