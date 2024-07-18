from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target_sum = total_sum // k
        nums.sort(reverse=True)
        n = len(nums)
        visited = [False] * n
        
        def backtrack(start, k_left, current_sum, cache):
            if k_left == 0:
                return True
            if current_sum == target_sum:
                return backtrack(0, k_left - 1, 0, cache)
            
            state = tuple(visited)
            if state in cache:
                return cache[state]
            
            for i in range(start, n):
                if not visited[i] and current_sum + nums[i] <= target_sum:
                    visited[i] = True
                    if backtrack(i + 1, k_left, current_sum + nums[i], cache):
                        cache[state] = True
                        return True
                    visited[i] = False
            
            cache[state] = False
            return False
        
        cache = {}
        return backtrack(0, k, 0, cache)
