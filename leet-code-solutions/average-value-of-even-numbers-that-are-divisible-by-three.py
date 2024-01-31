class Solution:
    def averageValue(self, nums: List[int]) -> int:
        counter=0 ; total=0
        for i in nums:
            if i%2==0 and i%3==0:
                counter+=1
                total+=i
        if total==0:
            return 0
        return total//counter
        