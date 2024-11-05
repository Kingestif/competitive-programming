class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        map = Counter(nums)

        if target in map:
            return True
        return False
