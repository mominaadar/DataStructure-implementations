class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return 
        
        last = self.head
        while last.next is not None:
            last = last.next
            
        last.next = new_node
        
        
    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp:
            ret_str += str(temp.val) + ", "
            temp = temp.next
            
        ret_str = ret_str.rstrip(', ')
        ret_str = ret_str + ']'
        return ret_str
        

    def pop(self):
        if self.head is None:
            raise Exception('List is already empty')
            
        if self.head.next is None:
            val = self.head.val
            self.head = None
            return val
        
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
            
        val = temp.val
        prev.next = None
        return val
        
        
    def insert(self, index, val):
        new_node = Node(val)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1
            
        new_node.next = temp
        prev.next = new_node
        
        
    def remove_at(self, index):
        if self.head is None:
            raise Exception('List is empty.')
            
        temp = self.head
        if index == 0:
            self.head = temp.next
            return
        
        counter = 0
        while temp is not None and counter<index:    
            prev = temp
            temp= temp.next
            counter += 1
        
        if temp is None:
            raise Exception("Index not found")
            
        prev.next = temp.next
        
    
    def remove(self, val):
        if self.head is None:
            raise Exception('List is empty')
            
        temp = self.head
        if temp is not None:
            if temp.val == val:
                self.head = temp.next #or self.head.next
                temp = None
                return
        
        while temp:
            if temp.val == val:
                break
                
            prev = temp
            temp = temp.next
            
        if temp is None:
            return 
        
        prev.next = temp.next    
    
        
    def length(self):
        temp = self.head
        counter = 0
        while temp:
            temp = temp.next
            counter += 1
            
        return counter
        
    
    
    def get_last(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            return
        
        temp = self.head.next
        
        while temp.next is not None:
            temp = temp.next
            
        return temp
    
    
    
    def reverse_list(self):
        last = self.get_last()
        size = self.length()
        
        if self.head is None or self.head.next is None:
            return
        
        new_head = last
        
        for i in range(size-1):
            temp = self.head
                    
            for i in range(size-1-i):
                if temp.next == last:
                    break
                else:
                    temp = temp.next
                    
            last = temp        
                    
            if new_head.next is None:
                new_head.next = last
                pos = last
            else:
                pos.next = last
                pos = last
        
        self.head = new_head
        last = pos
        last.next = None    


if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list() 
    print(l)

