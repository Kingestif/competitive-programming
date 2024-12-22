class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word1="qwertyuiopQWERTYUIOP"
        word2="asdfghjklASDFGHJKL"
        word3="zxcvbnmZXCVBNM"
        
        new=[]
        ch1=False
        ch2=False
        ch3=False
        for i in range(0,len(words)):
            ch1=False
            ch2=False
            ch3=False
            for j in range(0,len(words[i])):
                if(words[i][j] not in word1 and ch1==False):
                    ch1=True
                if(words[i][j] not in word2 and ch2==False):
                    ch2=True
                if(words[i][j] not in word3 and ch3==False):
                    ch3=True
        
            if(ch1==False or ch2==False or ch3==False):
                new.append(words[i])
            
        return new
