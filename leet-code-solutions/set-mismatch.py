class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        new=[]
        miss=0
        duplicate=0
        counter=0
        again={
        
        }
        for i in range(0,len(nums)):
            if(nums[i] not in again):
                again[nums[i]]=0
            else:
                # again[nums[i]]=again[nums[i]]+1
                again[duplicate]=nums[i]
        
        x=1
        nums=set(nums)
        for i in range(0,len(nums)+1):
            if(x not in nums):
                miss=x
            x+=1
        
        new.append(again[duplicate])
        new.append(miss)
        
        return new