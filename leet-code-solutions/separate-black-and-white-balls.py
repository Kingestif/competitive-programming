class Solution:
    def minimumSteps(self, s: str) -> int:
        start=0 ; end=1 ; counter=0
        new=list(s)
        while end < len(new):
            if new[start]=="1" and  new[end]=="0":
                new[start] , new[end]= new[end] ,new[start]
                start += 1
                end += 1
                counter += end - start
            elif new[start]=="1" and new[end] == "1":
                end += 1
            else:
                start += 1
                end += 1
        return counter



                


        