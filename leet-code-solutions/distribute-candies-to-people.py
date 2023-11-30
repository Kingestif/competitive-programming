class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        new=[0]*num_people
        inc=1
        check=True
        total=0
        while total<candies:
            if(check==False):
                break
            i=0
            while i<num_people:
                new[i]+=inc
                total=sum(new)
                print(total)
                if(total==candies):
                    check=False
                    break
                elif(total>candies):
                    new[i]=0
                    new[i]=candies-sum(new)
                    check=False
                    break

                inc+=1
                i+=1


        return new








