class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit=[]
        bit2=[]
        bit3=[]
        i=0
        counter=0
        while x>0 or y>0:
            if(x>=0):
                bit.append(x%2)
                x=x//2
            if(y>=0):
                bit2.append(y%2)
                y=y//2

            if(i<len(bit2) and i<len(bit)):
                if(bit[i]!=bit2[i]):
                    counter+=1
            i+=1


        bit.reverse()
        bit2.reverse()
        print(bit)    
        print(bit2)
        return counter