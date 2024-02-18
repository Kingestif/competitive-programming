class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map=defaultdict(int) ; total=0
        map[0]=1  ;  counter=0
        for i in range(len(nums)):
            total += nums[i]
            if total % k in map:
                counter += map[total % k]
            map[total % k] += 1                
        return counter