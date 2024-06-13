class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val]=len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        last_el = self.data[-1]
        ind_rem_el = self.map[val]
        self.map[last_el] = ind_rem_el
        self.data[ind_rem_el] = last_el
        self.data[-1]=val
        self.data.pop()
        self.map.pop(val)
        return True
    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
