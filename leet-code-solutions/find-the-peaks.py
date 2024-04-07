class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        for i in range(len(mountain)-1):
            if i == 0:
                continue
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                ans.append(i)

        return ans

