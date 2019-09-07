class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Ring:
    def __init__(self):
        self.head = None

    def __str__(self):
        ret = '['
        temp = self.head
        
        while temp:
            ret += str(temp.val) + ', '
            temp = temp.next
            
            if temp == self.head:
                break
            
        ret = ret.rstrip(', ')
        ret += ']'
        
        return ret
        
        
    def _get_last(self):
        if self.head is None:
            return 
        
        temp = self.head.next
        while temp.next != self.head:
            temp = temp.next
            
        return temp
        
    def insert(self, index, val):
        new_node = Node(val)
        last = self._get_last()
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            last.next = self.head
            return
        
        temp = self.head
        counter = 0
        
        while counter < index:
            prev = temp
            temp = temp.next
            counter += 1
        
        if new_node.next == self.head:
            self.head = new_node
        else:
            new_node.next = temp
            prev.next = new_node
            
            
    def remove(self,val):
        if self.head is None:
            return
        
        last = self._get_last()
        temp = self.head
        
        if temp.val == val:
            if last == self.head:
                self.head = None
            else:
                temp = temp.next
                self.head = temp
                last.next = self.head
            return
        
        prev = temp
        temp = temp.next
        
        while temp != self.head:
            if temp.val == val:
                break
            
            prev = temp
            temp = temp.next
                
        if temp == self.head:
            return
            
        prev.next = temp.next


    def remove_at(self, index):
        if self.head is None:
            return
        
        last = self._get_last()
        temp = self.head
        
        if index == 0:
            if last == self.head:
                self.head = None
            else:
                temp = temp.next
                self.head = temp
                last.next = self.head
            return
        
        temp = self.head
        count = 0

        while count < index:
            prev = temp
            temp = temp.next
            count += 1
            
        if temp == self.head:
            prev.next = temp.next
            self.head = temp.next
            
        prev.next = temp.next


    def len(self):
        last = self._get_last()
        
        if self.head is None:
            return 0
        
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
            
            if temp == self.head:
                break
        return count


    def get(self, index):
        if self.head is None:
            raise IndexError('List is empty')
            
        if index == 0:
            return self.head.val
        
        temp = self.head
        count = 0
        while count < index:
            temp = temp.next
            count += 1
            
        return temp.val


    def push(self,val):
        if self.head is None:
            self.insert(0,val)
            return
        else:
            length = self.len()
            
        count = 0
        temp = self.head
        while count < length:
            temp = temp.next 
            count += 1
        self.insert(count,val)
        
        
    def pop(self):
        if self.head is None:
            return
        else:
            length = self.len()
        
        temp = self.head
        count = 0
        
        while count < length:
            temp = temp.next
            count += 1
            
        print(self.get(length-1))
        self.remove_at(count-1)

if __name__ == '__main__': 
    r = Ring()
    r.insert(1, 1)
    r.insert(0, 1)
    r.insert(0, 2)
    r.insert(1, 3)
    r.insert(7, 5)  # different behavrior since it's a ring! 
    print(r)
