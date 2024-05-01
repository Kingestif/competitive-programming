class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        sum=x+y
        print(sum)
        sum=bin(sum)

        sum=sum[2:]
        return sum



