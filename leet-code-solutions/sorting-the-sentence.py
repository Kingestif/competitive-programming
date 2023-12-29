class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        sent=[0]*len(s)
        for i in range(len(s)):
            num=int(s[i][-1])
            print(num)
            sent[num-1]=s[i][:len(s[i])-1]

        print(sent)
        sent=" ".join(sent)
        return sent




        