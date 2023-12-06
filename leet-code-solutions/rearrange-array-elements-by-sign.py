class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        new1=[]
        new2=[]
        new3=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                new1.append(nums[i])
            else:
                new2.append(nums[i])
        
        for i in range(len(new1)):
            new3.append(new1[i])
            new3.append(new2[i])
        return new3

        