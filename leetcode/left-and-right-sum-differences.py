class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        v1 = []
        summ = 0
        for i in nums:
            v1.append(summ)
            summ += i

        summ = 0 ; v2 = []
        for i in range(len(nums)-1,-1,-1):
            v2.append(summ)
            summ += nums[i]
        v2.reverse()
        ans = []
        for i in range(len(v1)):
            ans.append(abs(v1[i] - v2[i]))

        return ans