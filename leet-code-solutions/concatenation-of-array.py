class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new=[]
        new.append(nums)
        new.append(nums)
        print(new)
        length=len(nums)*2
        x=[]

        for i in range(len(new)):
            for j in range(len(new[i])):
                x.append(new[i][j])
        return x