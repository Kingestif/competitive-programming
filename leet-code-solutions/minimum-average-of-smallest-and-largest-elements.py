class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        queue = deque(nums)
        average = []
        while queue:
            average.append((queue.popleft() + queue.pop())/2)
        return min(average)


