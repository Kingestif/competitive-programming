class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        prev = nums[0]
        sor = sorted(nums)
        count = 0
        if nums == sor:
            return 0
        for i in range(len(nums)):
            nums.append(nums.pop(0))
            count += 1
            if nums == sor:
                return len(nums) - count
        return -1
            