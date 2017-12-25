class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        if self.top is None:
            self.top = Element(data)
        else:
            aux = self.top
            self.top = Element(data)
            self.top.next = aux


    def pop(self):
        if self.top is None:
            return None

        aux = self.top

        if self.top.next is None:
            self.top = None
        else:
            self.top = self.top.next

        return aux


    def peek():
        return self.top
