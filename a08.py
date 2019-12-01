class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
        
        
    def _get_hash(self,key):
        count = 0
        
        if type(key) is int:
            return key % self.size
        
        elif type(key) is str:
            for i in range(len(key)):
                count += ord(key[i])
            return count % self.size
        
        elif type(key) is tuple:
            count = key[0] * key[1]
            return count % self.size
            
            
    def __str__(self):
        ret = ''
        
        for i, item in enumerate(self.map):
            if item is not None:
                ret += str(i) + ' : ' + str(item) + '\n'
        
        return ret
    


    def add(self,key,value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            return True
        
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
            
                    return True
        
        self.map[key_hash].append(key_value)
        return True
        

    def get(self,key):
        key_hash = self._get_hash(key)
        
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
            
        raise KeyError(str(key))
        
        
    def delete(self,key):
        key_hash = self._get_hash(key)
        
        if self.map[key_hash] is None:
            raise KeyError(str(key))
        
        else:
            for pair in range(len(self.map[key_hash])):
                if self.map[key_hash][pair][0] == key:
                    self.map[key_hash].pop(pair)
                    return True

if __name__ == '__main__': 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")

    print(h)
    