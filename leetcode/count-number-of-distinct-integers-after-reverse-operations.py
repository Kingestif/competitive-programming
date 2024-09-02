class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        for i in nums:
            reverse_num = int(str(i)[::-1])
            s.add(reverse_num)

        return len(s)