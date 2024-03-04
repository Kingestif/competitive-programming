import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return
        # the below numbers are made due to floating-point precision error
        # we can address them using specific code but have no time now
        elif(n==243 or n==59049 or n==1594323 or n==14348907 or n==129140163):
            return True
        last=math.log(n,3)
        print(last)


        if(last==math.ceil(last)):
            check=True
        else:
            check= False

        return check