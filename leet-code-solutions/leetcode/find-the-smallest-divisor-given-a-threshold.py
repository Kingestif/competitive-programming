import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def API(mid):
            total = 0
            for i in nums:
                total += math.ceil(i/mid)

            if total <= threshold:
                return True
            else:
                return False

        start = 1 ; end = max(nums)
        while start <= end:
            mid = (start + end) // 2
            if API(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start 