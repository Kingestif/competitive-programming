class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # x=list(words[1])
        # x.reverse()
        # return x
        map={}
        counter=0
        for i in words:
            y=list(i) 
            y.reverse()
            y="".join(y)

            if y not in map:
                map[i]=1
            else:
                counter+=1
        return counter

        