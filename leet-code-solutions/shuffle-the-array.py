class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new1=[]
        new2=[]
        new3=[]
        for i in range(n):
            new1.append(nums[i])

        for i in range(n,len(nums)):
            new2.append(nums[i])

        for i in range(n):
            new3.append(new1[i])
            new3.append(new2[i])

        return new3


