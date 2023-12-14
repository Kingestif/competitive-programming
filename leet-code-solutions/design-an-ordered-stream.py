class OrderedStream:
    # always use self if you want to access that variabel on differet class
    # Core:if current arr with the index is 0 return [] else iterate by concatenatib


    def __init__(self, n: int):
        self.index=0
        self.storage=[0]*n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.storage[idKey-1]=value
        
        if self.storage[self.index]==0:
            return []
        else:
            i=self.index
            new=[]
            while i<len(self.storage) and self.storage[i]!=0:
                new.append(self.storage[i])
                i+=1
                self.index=i
            return new
                
        # return self.storage[self.index]



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)