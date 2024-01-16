class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0 ; new=[]
        for i in nums:
            total+=i
            new.append(total)
        return new