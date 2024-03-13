from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        map=defaultdict(int)
        start=0 ; end=0 ; counter=0

        while end < len(nums):
            map[nums[end]] += 1
            end += 1
            
            while len(map) >= distinct:
                counter += len(nums) - end + 1
                map[nums[start]] -= 1
                if map[nums[start]] <= 0:
                    del map[nums[start]]
                start += 1

        return counter


