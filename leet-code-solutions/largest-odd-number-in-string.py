class Solution:
    def largestOddNumber(self, num: str) -> str:
        num=str(num)
        s=""
        x=-1
        for i in range(len(num)):
            if(int(num[x])%2!=0):
                if(x==-1):
                    return num
                else:
                    ans=num[0:(x+1)]
                    return ans
            x-=1

        return ""