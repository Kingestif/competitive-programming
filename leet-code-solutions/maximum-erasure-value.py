from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start=0 ; end=0 ; value=0 ; max=float("-inf")
        map=defaultdict(int) 
        while end<len(nums):
            if nums[end] not in map:
                value+=nums[end]
                map[nums[end]]+=1
                end+=1
            else:
                if value > max: 
                    max=value

                value-=nums[start]

                map[nums[start]]-=1
                if map[nums[start]]<=0:
                    del map[nums[start]]
                    
                start+=1

        if value > max:
            max=value

        return max