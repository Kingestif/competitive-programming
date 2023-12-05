class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        x=0
        new=[]
        for i in range(len(nums)):
            if x%2!=0:
                new+=[nums[i]]*nums[i-1]
            x+=1

        return new