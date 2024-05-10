class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # Core: for every Xor beauty ((nums[i] | nums[j]) & nums[k]) there is another Xor beautry with same value so no need to do all that operation jsut xor them to eliminate this same values and return the left one
        val = 0
        for i in nums:
            val ^= i

        return val
