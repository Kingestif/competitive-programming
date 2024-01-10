class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])  # Calculate the sum of the first k elements
        max_sum = curr_sum
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]  # Update the current sum
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum / k

