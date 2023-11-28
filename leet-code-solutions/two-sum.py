class Solution(object):
    def twoSum(self, nums, target):
        new=[]
        map={}
        for i in range(0,len(nums)):
            if(target-nums[i] not in map):
                map[nums[i]]=i
            else:
                new.append(map[target-nums[i]])
                new.append(i)

        return new



