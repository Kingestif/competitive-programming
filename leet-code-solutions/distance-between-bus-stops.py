class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # the starting index must be lessthan ending
        if start>destination:
            start,destination=destination,start

        total=0
        total2=0

        # just find the distance b/n them normal way
        for i in range(start,destination):
            total+=distance[i]

        # adds the distance the other way(behind one )
        i=-1 ; j=0
        for j in range(len(distance)):
            if j < start:
                total2+=distance[j] 

        for j in range(len(distance)):
            if j >= destination:
                total2+=distance[j]

        if total<total2:
            return total
        else:
            return total2