class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None


    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    
    def search(self, data):
        if self.head is None:
            return None
        
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return current_node

            current_node = current_node.next

        return None


    def remove(self, data):
        if self.head is None:
            return None

        current_node = self.head
        
        if current_node.data == data:
            if self.last.data == data:
                self.head = None
                self.last = None
            else:
                self.head = current_node.next
                del current_node
            return True
        
        previous_node = None

        while current_node is not None:
            if current_node.data == data:
                if current_node == self.last:
                    self.last = previous_node
                    self.last.next = None
                else:
                    previous_node.next = current_node.next

                del current_node
                return True

            previous_node = current_node
            current_node = current_node.next

        return False


    def show_list(self):
        current_node = self.head

        while current_node is not None:
            print current_node.data,
            current_node = current_node.next

        print
