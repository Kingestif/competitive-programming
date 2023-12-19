from collections import defaultdict
import copy
class Bitset:

    def __init__(self, size: int):
        self.counter=0
        self.map=defaultdict(int)
        self.map2=defaultdict(int)
        self.size=size
        self.flipped=False

    def fix(self, idx: int) -> None:
        if self.flipped==False:
            if self.map[idx]==0:
                self.counter+=1

            self.map[idx]=1
            self.map2[idx]=0
        else:
            # since defaultdict gives default 1 even if not present
            if idx in self.map2:
                if self.map2[idx]==0:
                    self.counter+=1


            self.map[idx]=0
            self.map2[idx]=1


    def unfix(self, idx: int) -> None:
        if self.flipped==False:
            if self.map[idx]==1:
                self.counter-=1

            self.map[idx]=0
            self.map2[idx]=1
        else:
        #    **since not exist keys are 1 
            if idx not in self.map2:
                self.counter-=1
            elif self.map2[idx]==1:
                self.counter-=1


            self.map[idx]=1
            self.map2[idx]=0

    def flip(self) -> None:
        self.flipped = not self.flipped   
        self.counter=self.size - self.counter 

    def all(self) -> bool:
        if self.counter == self.size:
            return True
        else:
            return False

    def one(self) -> bool:
        if self.counter >= 1:
            return True
        else:
            return False

    def count(self) -> int:
        return self.counter
        

    def toString(self) -> str:
        print(self.counter)
        s=""
        
        if self.flipped==False:
            print(self.map,self.map2)
            for i in range(self.size):
                if i not in self.map:
                    s+='0'
                else:
                    s+=str(self.map[i])
            return s
        else:
            for i in range(self.size):
                if i not in self.map2:
                    s+='1'
                else:
                    s+=str(self.map2[i])
            return s

        

        
        

        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flipped()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()