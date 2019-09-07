class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def push(self,val=None):
        new_node = Node(val)
        
        if self.head is None: #empty list
            self.head = new_node
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
            
        last.next = new_node
        
        
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
    
    
    def __str__(self):
        ret_str = '['
        
        temp = self.head
        while temp:
            ret_str += str(temp.val) + ', '
            temp = temp.next
            
        ret_str = ret_str.rstrip(', ')
        ret_str = ret_str + ']'
        return ret_str
    
    
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
            
        prev.next = new_node
        new_node.next = temp


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
    
    
    def len(self):
        temp = self.head
        counter = 0
        
        while temp:
            temp = temp.next
            counter += 1
            
        return counter
    
    
    def get(self,index):
        if index == 0:
            return self.head.val
            
        temp = self.head
        count = 0
        while temp is not None and count<index:
            temp = temp.next
            count += 1

            if count == index:
                if temp is not None:
                     return temp.val
                else:
                    raise IndexError('Index not found')
                
        if count != index:
            raise IndexError('Index not found')


if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    print(l)

    print(l.len())

    l.pop() 
    print(l.len())

    print(l.get(0))
    l.get(2) # Should say "IndexError: Index out of bound"

