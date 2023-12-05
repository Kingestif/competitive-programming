class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word1="qwertyuiopQWERTYUIOP"
        word2="asdfghjklASDFGHJKL"
        word3="zxcvbnmZXCVBNM"
        
        new=[]
        # words = ["adsdf","sfd"]
        ch1=False
        ch2=False
        ch3=False
        # print(words[1][2] in words[1])
        # print(len(words[1]))
        for i in range(0,len(words)):
            ch1=False
            ch2=False
            ch3=False
            for j in range(0,len(words[i])):
                # print(words[i][j])
                if(words[i][j] not in word1 and ch1==False):
                    ch1=True
                if(words[i][j] not in word2 and ch2==False):
                    ch2=True
                if(words[i][j] not in word3 and ch3==False):
                    ch3=True
        
            if(ch1==False or ch2==False or ch3==False):
                new.append(words[i])
                # print(words[i])
            # print(ch1,ch2,ch3)
            
        return new
        # print(word1)
