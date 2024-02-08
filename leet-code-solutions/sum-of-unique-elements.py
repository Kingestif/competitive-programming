from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        map=defaultdict(int)
        for i in nums:
            map[i] += 1

        counter=0
        for key,values in map.items():
            if values == 1:
                counter+=key

        return counter
        