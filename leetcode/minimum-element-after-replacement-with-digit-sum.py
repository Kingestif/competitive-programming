class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            summ = 0
            for j in range(len(str(i))):
                summ += int(str(i)[j])

            ans.append(summ)

        return min(ans)

        