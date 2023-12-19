import random
class RandomizedSet:

    def __init__(self):
        self.num=set()
        

    def insert(self, val: int) -> bool:
        if val not in self.num:
            self.num.add(val)
            return True
        else:
            return False



    def remove(self, val: int) -> bool:
        if val in self.num:
            self.num.discard(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_element = random.choice(list(self.num))
        return random_element



        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()