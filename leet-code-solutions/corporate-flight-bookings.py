class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        start=0 ; end=0 ; value=0
        new=[0]*n
        for i in range(len(bookings)):
            start=bookings[i][0] ; end=bookings[i][1] ; value=bookings[i][2]
            print(start,end,value)
            new[start-1]+=value 

            if end<n:
                new[end]+=value*-1

        print(new)
        total=0 ; max=float('-inf')

        for i in range(len(new)):
            total+=new[i]
            new[i]=total
            if new[i] > max:
                max=new[i]


        return new






