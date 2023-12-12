class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        start=nums[0]
        counter=1
        nums=list(nums)
        nums.sort()
        
        max=float('-inf')
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                counter+=1
            elif(nums[i]!=nums[i-1]):
                if counter > max:
                    max=counter
                counter=1
        
            if i >= len(nums)-1 and counter>max:
                max=counter
        
        # print(counter)
        return max
        # print(nums)
        
        
        
        