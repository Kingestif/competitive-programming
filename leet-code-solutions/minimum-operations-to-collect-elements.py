class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        check = set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] <= k and nums[i] not in check:
                count += 1
                last = i
                check.add(nums[i])
        return len(nums) - last


