class Solution:
    def totalMoney(self, n: int) -> int:

        total=0;inc=0;i=0
        counter=1
        money=1
        z=8
        while i < n:
            total+=counter
            counter+=1
            if counter==inc+z:
                money+=1
                counter=money
                z+=1

            i+=1
        return total













