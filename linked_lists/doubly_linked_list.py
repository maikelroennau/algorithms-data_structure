class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None


    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
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

        while current_node is not None:
            if current_node.data == data:
                if current_node == self.last:
                    self.last = current_node.prev
                    self.last.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev

                del current_node
                return True

            current_node = current_node.next

        return False


    def show_list(self):
        current_node = self.head

        while current_node is not None:
            print current_node.data,
            current_node = current_node.next

        print
