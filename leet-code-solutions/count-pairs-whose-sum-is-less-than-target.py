class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        start=0 ; end=len(nums)-1 ; nums.sort()
        counter=0
        while start<end:
            if nums[start] + nums[end] >=target:
                end-=1
            else:
                counter+=end-start
                start+=1
        return counter

        