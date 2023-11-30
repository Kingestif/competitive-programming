class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x=num
        i=num+1
        y=i
        counter=1
        check=True
        ans=0
        while check:
            j=0
            if(check==False):
                break
            while j<t:
                i-=1
                num+=1

                j+=1

            if(i==num):
                return ans
                check=False
                break
            # i+=1
            i=y+counter
            ans=i
            num=x
            counter+=1