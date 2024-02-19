class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        map=defaultdict(int) ; total=0
        map[0]=1  ;  counter=0
        for i in range(len(nums)):
            total += nums[i]
            if total - goal in map:
                counter += map[total - goal]
            map[total] += 1                
        return counter