class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        i=0 ;j=0
        while i<len(word1) or j < len(word2):
            if(i<len(word1)):
                w1+=word1[i]
            if(j<len(word2)):
                w2+=word2[j]
            i+=1 ; j+=1

        return w1==w2




