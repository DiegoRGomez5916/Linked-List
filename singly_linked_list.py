import node

class Singly_Linked_List:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()
    
    def search(self, target):
        curr = self.head
        while curr is not None:
            if curr.data == target:
                return True
            curr = curr.next
    
    def get_length(self):
        curr = self.head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length
    
    def prepend(self, data):
        new_node = node.Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node = node.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def insert_at(self, data, pos):
        if pos <= 0:
            self.prepend(data)
            return
        
        previous = self.head
        count = 0
        while (count < (pos - 1)) and (previous is not None):
            previous = previous.next
            count += 1
        
        if previous is None:
            self.append(data)
            return
        
        new_node = node.Node(data)
        new_node.next = previous.next
        previous.next = new_node
    
    def delete_head(self):
        if self.head is None:
            return None
        
        self.head = self.head.next
    
    def delete_tail(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            return None
        
        penultimate_node = self.head
        while penultimate_node.next.next is not None:
            penultimate_node = penultimate_node.next
        
        penultimate_node.next = None
    
    def delete_at(self, pos):
        if pos <= 0:
            self.delete_head()
            return
        
        previous = self.head
        count = 0
        while (count < (pos - 1)) and (previous is not None):
            previous = previous.next
            count += 1
        
        if previous is None:
            self.delete_tail()
            return
        
        previous.next = previous.next.next

if __name__ == '__main__':
    new_linked_list = Singly_Linked_List()
    new_linked_list.append(2)
    new_linked_list.traverse()
    new_linked_list.prepend(10)
    new_linked_list.traverse()
    new_linked_list.insert_at(5, 1)
    new_linked_list.traverse()
    new_linked_list.insert_at(21, 10)
    new_linked_list.traverse()
    new_linked_list.insert_at(1, -1)
    new_linked_list.traverse()
    new_linked_list.delete_at(1)
    new_linked_list.traverse()
    new_linked_list.delete_head()
    new_linked_list.traverse()
    new_linked_list.delete_tail()
    new_linked_list.traverse()
    new_linked_list.delete_at(-1)
    new_linked_list.traverse()
    new_linked_list.delete_at(10)
    new_linked_list.traverse()
