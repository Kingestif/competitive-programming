class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i=0
        original=capacity
        counter=0
        map={}
        while i<len(plants):
            if(i not in map):

                if(capacity>=plants[i]):
                    map[i]=0
                    counter+=1
                    capacity-=plants[i]
                    i+=1
                else:
                    counter+=i
                    i=0
                    capacity=original
            else:
                i+=1
                counter+=1

        return counter

