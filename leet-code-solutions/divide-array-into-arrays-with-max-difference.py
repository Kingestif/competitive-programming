class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums)==0:
            return nums
        nums.sort()
        start=0 ; end=2

        while end < len(nums):
            if nums[end] - nums[start] > k:
                return []
            end+=3 ; start+=3
        
        print("yes")
        counter=0; arr=[]
        three=[]
        for i in nums:
            if counter<3:
                three.append(i)
                counter+=1
            else:
                counter=1
                arr.append(three)
                three=[]
                three.append(i)
        arr.append(three)
        return arr
