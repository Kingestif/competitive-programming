class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        summ = 0
        start = 0
        end = len(nums) - 1
        while start < end:
            val = str(nums[start]) + str(nums[end])
            summ += int(val)
            start += 1
            end -= 1

        if start == end:
            summ += nums[start]

        return summ
        

        