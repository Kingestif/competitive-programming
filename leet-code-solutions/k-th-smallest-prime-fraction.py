class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans = []
        for i in arr:
            for j in arr:
                ans.append((i/j,[i,j]))

        ans.sort()
        return ans[k-1][1]