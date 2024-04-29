class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s1 = set(nums[0])
        for i in range(1,len(nums)):
            s2 = set(nums[i])
            s1 = s1.intersection(s2)


        if len(s1) == 0:
            return []

        s1 = list(s1)
        s1.sort()
        return s1