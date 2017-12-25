class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None


    def add(self, data):
        if self.first is None:
            self.first = Element(data)
            self.last = self.first
        else:
            self.last.next = Element(data)
            self.last = self.last.next


    def remove(self):
        if self.first is None:
            return None

        if self.first == self.last:
            aux = self.first
            self.first = None
            self.last = None
            return aux
        else:
            aux = self.first
            self.first = self.first.next
            return aux
