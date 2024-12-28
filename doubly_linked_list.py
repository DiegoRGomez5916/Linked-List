import node

class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, data):
        new_node = node.Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    
    def append(self, data):
        new_node = node.Node(data)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def insert_at(self, data, pos):
        new_node = node.Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif pos <= 0:
            self.prepend(data)
        else:
            curr = self.head
            count = 0
            while (count < pos) and (curr is not None):
                curr = curr.next
                count += 1
            
            if curr is None:
                self.append(data)
            else:
                new_node.previous = curr.previous
                new_node.next = curr
                curr.previous.next = new_node
                curr.previous = new_node
    
    def delete_head(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
            self.head.previous = None
    
    def delete_tail(self):
        if self.tail == None:
            return
        else:
            self.tail = self.tail.previous
            self.tail.next = None
    
    def delete_at(self, pos):
        if self.head == None:
            return
        elif pos <= 0:
            self.delete_head()
        else:
            curr = self.head
            count = 0
            while (count < pos) and (curr is not None):
                curr = curr.next
                count += 1
            
            if curr is None:
                self.delete_tail()
            else:
                curr.previous.next = curr.next
    
    def search(self, target):
        curr = self.head
        while (curr is not None) and (curr.data != target):
            curr = curr.next
        
        return curr
    
    def get_length(self):
        curr = self.head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        return count
    