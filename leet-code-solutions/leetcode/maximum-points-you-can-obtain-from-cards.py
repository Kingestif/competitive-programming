class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        start=0 ; k=k-1   ; j=len(cardPoints)-1 ; start=0   
        arr=[] ; max=float('-inf')
        prefixfront=[] ; prefixback=[]
        total=0
        for i in cardPoints:
            total+=i
            prefixfront.append(total)
        
        total=0
        for i in range(len(cardPoints)-1,-1,-1):
            total+=cardPoints[i]
            prefixback.append(total)
        prefixback.reverse()
        print(prefixfront, prefixback)

        final=[]
        while True:
            if start==0:
                if prefixfront[k] > max:
                    max=prefixfront[k]
                start+=1
                k-=1
            elif k < 0:
                if prefixback[j] > max:
                    max= prefixback[j]
                break
            else:
                if prefixfront[k]+prefixback[j] > max:
                    max=prefixfront[k]+prefixback[j]
                k-=1 ; j-=1
        return max


        


