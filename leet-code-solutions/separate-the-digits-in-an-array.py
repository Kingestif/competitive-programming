class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        ans = []
        for i in nums:
            arr.append(list(str(i)))

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                ans.append(int(arr[i][j]))
        return ans
