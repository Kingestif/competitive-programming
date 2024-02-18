class Solution:
    def bestClosingTime(self, customers: str) -> int:
        preY=[] ; total=0 ; preN=[] ; total1=0 ; count=[]
        for i in customers:
            if i == "Y":
                total += 1
            else:
                total1 += 1
            preY.append(total)
            preN.append(total1)
        print(preY,preN)

        count.append(preY[-1])
        for i in range(len(customers)):
            if customers[i] == "Y":
                count.append(preY[-1] - preY[i] + preN[i])
            else:
                count.append(preN[i] + (preY[-1] - preY[i]))

        print(count)
        return count.index(min(count))
        
        