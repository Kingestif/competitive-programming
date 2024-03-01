from collections import defaultdict
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        map=defaultdict(int)
        for i in nums:
            map[i] += 1

        for key, values in map.items():
            if values > 2:
                return False

        return True
