class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        map = defaultdict(list)
        for i in range(len(nums)):
            map[abs(nums[i])].append(nums[i])
        return max(map[min(map)])
