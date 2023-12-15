from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.map={}
        self.map2 = defaultdict(int)

    def add(self, number: int) -> None:
        if number not in self.map:
            self.map[number]=1
        else:
            self.map2[self.map[number]]-=1
            self.map[number]+=1

        self.map2[self.map[number]]+=1
        

    def deleteOne(self, number: int) -> None:
        if number in self.map:
            self.map2[self.map[number]]-=1
            self.map[number]-=1
            self.map2[self.map[number]]+=1


            if self.map[number]<=0:
                del self.map[number]

    def hasFrequency(self, frequency: int) -> bool:
        # if frequency in self.map2:
        #     return True
        # else:
        #     return False
        print(self.map2)
        return self.map2[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)