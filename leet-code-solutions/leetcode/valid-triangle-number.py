class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        total=0
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            start=0 ; end = i-1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    total += end - start
                    end -= 1
                else:
                    start += 1
        return total 
        


