class Solution:
    def findMin(self, nums: List[int]) -> int:
        # case 1: if mid > last e/t end it means, our search space to to shift to the left
        # case 2: if mid < last we need to shift to the left
        start = 0 ; end = len(nums) - 1 ; minn = float('inf')
        while start <= end:
            mid = (start + end) //2
            # print(nums[mid])
            if nums[mid] < minn:
                minn = nums[mid]
            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1

        print("min",minn)
        # return 0
        return minn
