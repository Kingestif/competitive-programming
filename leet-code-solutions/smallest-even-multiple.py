class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        sx=[]
        start=2
        check=True
        if(n==1):
            return start
        while check:
            sx.append(n)
            if(start in sx):
                return start
            # print(n)
            n+=n
            start+=2



