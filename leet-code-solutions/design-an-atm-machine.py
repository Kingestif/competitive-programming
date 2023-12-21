from collections import defaultdict
class ATM:
    # Core: on Widthdraw: lets say amout = 5000 then check 5000//500 to know how many notes of 500 you need here 10 if you deposited that much or above then you have enough but if not next check with 200

    def __init__(self):
        self.map=[20,50,100,200,500]
        self.map2=defaultdict(int)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.map2[self.map[i]]+=banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        self.map3=[0]*5
        x=4
        default=self.map2.copy()
        while x>=0:
            needed=amount//self.map[x]
            if needed <= self.map2[self.map[x]]:
                self.map3[x]=needed
                self.map2[self.map[x]]-=needed
                if amount%self.map[x]==0: #if even then amount is covered
                    return self.map3
                else:   #there is still amount to be coverd
                    amount=amount - (self.map[x]*needed)
                    x-=1

            else:
                self.map3[x]=self.map2[self.map[x]]
                self.map2[self.map[x]]=0
                amount=amount - (self.map[x] * self.map3[x])
                x-=1

        self.map2=default.copy() #to restore subtructed values
        return [-1]
            



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)