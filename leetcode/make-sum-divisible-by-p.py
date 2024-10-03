from collections import defaultdict
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = [] ; total = 0     ; map = defaultdict(int)   
        for i in nums:
            total += i
            prefix.append(total)
        map[sum(nums) % p] = 0

        if total % p == 0:
            return 0

        summ = sum(nums)  ; mini = float('inf')   

        for i in range(len(prefix)):
            if prefix[i] % p in map:
                mini = min(mini, i + 1 - map[prefix[i] % p] )
            map[((summ % p) + (prefix[i] % p)) % p] = i + 1

        if mini == float('inf') or mini >= len(nums):
            return -1
            
        return mini


# why map[0] = -1

# it should be totalsum % p

# mini = min(mini, i - map[prefix[i] % p])
# i+1 argew

# map[((summ % p) + (prefix[i] % p)) % p] = i
# same here (i+1)

            