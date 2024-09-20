class Solution:
    def candy(self, ratings: List[int]) -> int:
        new=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                new[i]=new[i-1]+1

        ratings.reverse()
        new.reverse()

        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1] and new[i]<=new[i-1]):
                new[i]=new[i-1]+1

        return sum(new)     