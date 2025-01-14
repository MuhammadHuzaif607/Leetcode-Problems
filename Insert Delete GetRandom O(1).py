import random
class RandomizedSet:

    def __init__(self):
        self.idx_map = {}
        self.lst = []

    def insert(self, val: int) :
        if val in self.idx_map:
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True
        
        

    def remove(self, val: int) :
        if val not in self.idx_map:
            return False
        
        
        idx = self.idx_map[val]
        self.lst[idx] = self.lst[-1]
        self.idx_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.idx_map[val]
        return True


        

    def getRandom(self) :
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
# param_3 = obj.getRandom()


