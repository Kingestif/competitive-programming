class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map={}
        new=[]
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]]=1
            else:
                map[nums[i]]+=1

        for key,values in map.items():
            if values == 1:
                return key