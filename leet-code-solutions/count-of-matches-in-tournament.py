class Solution:
    def numberOfMatches(self, n: int) -> int:
        total=0
        while n!=1:
            if(n%2==0):
                matches=n/2
                n=n/2
                total+=matches
            else:
                matches=(n - 1) / 2
                n=(n - 1) / 2  + 1
                total+=matches

        return int(total)