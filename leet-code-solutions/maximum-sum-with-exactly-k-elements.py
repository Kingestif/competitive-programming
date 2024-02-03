class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxxi=max(nums) ; total=0
        while k>0:
            total+=maxxi
            maxxi+=1
            k-=1
        return total
            