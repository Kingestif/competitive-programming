class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # bin=[0]*len(flips)
        # counter=0
        # for i in range(len(flips)):
        #     bin[flips[i]-1]=1
        #     check=bin[:i+1]
        #     if sum(check)==len(check):
        #         counter+=1
        # return counter
        # small=float('-inf')
        counter=0
        sum=0
        fsum=0
        for i in range(1,len(flips)+1):
            sum+=i
            fsum+=flips[i-1]
            if sum==fsum:
                counter+=1
        return counter

        



        