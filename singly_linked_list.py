import node

class Singly_Linked_List:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        """
        Prints out every node in the singly linked list on a single line
        """
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()
    
    def search(self, target):
        """
        Searches for a node containing a specific piece of data

        Args:
            target (any): data that will be searched for

        Returns:
            bool: returns true if the value was found and false if not found
        """
        curr = self.head
        while curr is not None:
            if curr.data is target:
                return True
            curr = curr.next
        return False
    
    def get_length(self):
        """
        Calculates the length of the linked list

        Returns:
            int: integer representing the length of the list
        """
        curr = self.head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length
    
    def prepend(self, data):
        """
        Adds a node at the head of the linked list

        Args:
            data (any): data that will be stored in the node
        """
        new_node = node.Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        """
        Adds a node at the tail of the linked list

        Args:
            data (any): data that will be stored in the node
        """
        new_node = node.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def insert_at(self, data, pos):
        """
        Adds a node at the specified position

        Args:
            data (any): data that will be stored in the node
            pos (int): the position where the data will be inserted(0 being the head of the list)
        """
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
        """
        Deletes the node at the head of the linked list

        Returns:
            returns: returns the node that was removed or None if the list is empty
        """
        if self.head is None:
            return None
        
        temp = self.head
        self.head = temp.next
        return temp
    
    def delete_tail(self):
        """
        Deletes the node at the tail of the linked list

        Returns:
            node: returns the node that was removed or None if the list is empty
        """
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        
        penultimate_node = self.head
        while penultimate_node.next.next is not None:
            penultimate_node = penultimate_node.next
        
        temp = penultimate_node.next
        penultimate_node.next = None
        return temp
    
    def delete_at(self, pos):
        """
        Deletes the node at the specified position

        Args:
            pos (int): the position where the node will be deleted

        Returns:
            node: returns the node that was removed or None if the list is empty
        """
        if pos <= 0:
            return self.delete_head()
        
        previous = self.head
        count = 0
        while (count < (pos - 1)) and (previous is not None):
            previous = previous.next
            count += 1
        
        if previous is None:
            return self.delete_tail()
        
        temp = previous.next
        previous.next = previous.next.next
        return temp

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
