class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None


    def add(self, data, node=None):
        if self.root is None:
            self.root = Node(data)
        else:
            if node is None:
                node = self.root

            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.add(data, node.left)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.add(data, node.right)


    def course_prefixed(self, node=None, sequence=[]):
        if self.root is None:
            return None

        if not node:
            node = self.root

        sequence.append(node)

        if node.left is not None:
            self.course_prefixed(node.left, sequence)

        if node.right is not None:
            self.course_prefixed(node.right, sequence)

        return sequence


    def course_infixed(self, node=None, sequence=[]):
        if self.root is None:
            return None

        if not node:
            node = self.root

        if node.left is not None:
            self.course_infixed(node.left, sequence)

        sequence.append(node)

        if node.right is not None:
            self.course_infixed(node.right, sequence)

        return sequence


    def course_postfixed(self, node=None, sequence=[]):
        if self.root is None:
            return None

        if not node:
            node = self.root

        if node.left is not None:
            self.course_postfixed(node.left, sequence)

        if node.right is not None:
            self.course_postfixed(node.right, sequence)

        sequence.append(node)

        return sequence


    def search(self, data, node=None):
        if self.root is None:
            return None

        if not node:
            node = self.root

        if data == node.data:
            return node

        if data < node.data:
            if node.left is not None:
                return self.search(data, node.left)
        elif node.right is not None:
            return self.search(data, node.right)

        return None


    def get_root(self):
        return self.root
