class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # easy
        map = defaultdict(int)
        for i in nums:
            map[i] += 1

        start = 1
        while True:
            if start not in map:
                return start
            else:
                start += 1
                
                        