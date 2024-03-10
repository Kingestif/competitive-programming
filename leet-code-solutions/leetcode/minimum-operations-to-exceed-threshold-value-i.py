class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        print(nums)
        counter = 0
        while True:
            if nums[-1] < k:
                nums.pop()
                counter += 1
            else:
                break

        return counter