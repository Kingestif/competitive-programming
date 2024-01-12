class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # we calculate for case True and False individually
        start=0 ; end=0 ; counter=0 ; max1=float('-inf') ; max2=float('-inf')
        tcount=0 ; fcount=0
        while end<len(answerKey):
            if answerKey[end]=='F':
                counter+=1
                end+=1
            else:
                if tcount<k:
                    counter+=1
                    if answerKey[end]=='T':
                        tcount+=1
                    end+=1
                else:
                    if counter>max1:
                        max1=counter
                    counter-=1
                    if answerKey[start]=='T':
                        tcount-=1
                    start+=1

        if counter>max1:
            max1=counter

        # return max1
        start=0 ; end=0 ; counter=0 ; max2=float('-inf')
        tcount=0 ; fcount=0

        while end<len(answerKey):
            if answerKey[end]=='T':
                counter+=1
                end+=1
            else:
                if fcount<k:
                    counter+=1
                    if answerKey[end]=='F':
                        fcount+=1
                    end+=1
                else:
                    if counter>max2:
                        max2=counter
                    counter-=1
                    if answerKey[start]=='F':
                        fcount-=1
                    start+=1

        if counter>max2:
            max2=counter

        print(max1,max2)
        if max1>max2:
            return max1
        else:
            return max2





        