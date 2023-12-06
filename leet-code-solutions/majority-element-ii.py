class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map={}
        new=[]
        test=len(nums)/3
        for i in range(len(nums)):
            if(nums[i] not in map):
                map[nums[i]]=1
            else:
                map[nums[i]]+=1

        for key,value in map.items():
            if value > test:
                new.append(key)
        return new


        


