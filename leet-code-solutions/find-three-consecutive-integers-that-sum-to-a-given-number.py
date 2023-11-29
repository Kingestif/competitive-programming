class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        new=[0]*3
        if(num%3==0):
            new[0]=num//3 - (1)
            new[1]=num//3 
            new[2]=num//3 + (1)

            return new