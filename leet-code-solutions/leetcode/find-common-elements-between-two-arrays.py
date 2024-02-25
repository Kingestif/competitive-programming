from collections import defaultdict
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map=defaultdict(int)
        map2=defaultdict(int)
        for i in nums1:
            map[i] += 1

        for i in nums2:
            map2[i] += 1

        counter = 0
        for i in map:
            if i in map2:
                counter += map[i]

        counter2 = 0
        for i in map2:
            if i in map:
                counter2 += map2[i]

        return [counter,counter2]
