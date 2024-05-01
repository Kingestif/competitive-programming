class Solution:
    def findComplement(self, num: int) -> int:
        bit=[]
        counter=0
        i=0
        while num>0:
            bit.append(num%2)
            num=num//2
            if(bit[i]==0):
                bit[i]=1
            else:
                bit[i]=0
            i+=1

        # bit.reverse()
        # print(bit)

        num=1
        counter=0
        for i in range(0,len(bit)):
            counter=counter + bit[i]*num
            num=num*2

        return counter



