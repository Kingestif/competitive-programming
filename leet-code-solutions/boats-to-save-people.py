class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        start=0 ; end=len(people)-1 ; people.sort()
        counter=0
        while start<end:
            if people[start] + people[end] <=limit:
                counter+=1
                people[start]=float('inf')
                people[end]=float('inf')
                start+=1 ; end-=1

            else:
                end-=1

        for i in people:
            if i!=float('inf'):
                counter+=1
        return counter



        