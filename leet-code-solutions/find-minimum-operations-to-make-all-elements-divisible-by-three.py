class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i%3 == 0:
                continue
            elif (i + 1)%3 == 0:
                count += 1
            elif( i-1) %3 == 0:
                count += 1
        return count
        