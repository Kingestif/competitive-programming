class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        start = 0   ;   end = 0     ;   mx = float('-inf')
        while start <= end and end< len(nums):
            if map[nums[end]] < k:
                mx = max(mx,end - start)
                map[nums[end]] += 1
                end += 1
            else:
                mx = max(mx,end - start)
                map[nums[start]] -= 1
                start += 1
        mx = max(mx,end - start)
        return mx
        
            