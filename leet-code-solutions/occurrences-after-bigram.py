class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text=text.split()
        new=[]
        for i in range(len(text)):
            if(text[i]==first and i!=len(text)-1 and text[i+1]==second):
                if(i+2<len(text)):
                    new.append(text[i+2])
        return new
