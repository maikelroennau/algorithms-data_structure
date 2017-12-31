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


    def remove(self, data, node=None, parent=None):
        if self.root is None:
            return None

        if not node:
            node = self.root

        if data == node.data:
            if node.left is None and node.right is None:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None

                del node
                return True

            if node.left is None and node.right is not None or node.left is not None and node.right is None:
                if parent:
                    if parent.left == node:
                        parent.left = node.left
                    else:
                        parent.right = node.right

                del node
                return True

            if node.left is not None and node.right is not None:
                moving_node = self.find_sucessor(node.right)
                moving_parent = self.find_parent(moving_node.data)

                node.data = moving_node.data

                if moving_parent.left == moving_node:
                    moving_parent.left = None
                else:
                    moving_parent.right = None

                del moving_node
                return True

        if data < node.data:
            if node.left is not None:
                return self.remove(data, node.left, node)
        elif node.right is not None:
            return self.remove(data, node.right, node)

        return False


    def find_parent(self, data, node=None, parent=None):
        if self.root is None:
            return None

        if data == self.root.data:
            return None

        if not node:
            node = self.root

        if data == node.data and parent is not None:
            return parent

        if data < node.data:
            if node.left is not None:
                return self.find_parent(data, node.left, node)
        elif node.right is not None:
            return self.find_parent(data, node.right, node)

        return None


    def find_sucessor(self, node):
        if node is None:
            return None

        if node.left is not None:
            return self.find_sucessor(node.left)
        else:
            return node


    def course_prefixed(self, node=None, sequence=[]):
        if self.root is None:
            return None

        if not node:
            node = self.root
            sequence = []

        sequence.append(node)

        if node.left is not None:
            self.course_prefixed(node.left, sequence)

        if node.right is not None:
            self.course_prefixed(node.right, sequence)

        del node
        return sequence


    def course_infixed(self, node=None, sequence=[]):
        if self.root is None:
            return None

        if not node:
            node = self.root
            sequence = []

        if node.left is not None:
            self.course_infixed(node.left, sequence)

        sequence.append(node)

        if node.right is not None:
            self.course_infixed(node.right, sequence)

        del node
        return sequence


    def course_postfixed(self, node=None, sequence=[]):
        if self.root is None:
            return None

        if not node:
            node = self.root
            sequence = []

        if node.left is not None:
            self.course_postfixed(node.left, sequence)

        if node.right is not None:
            self.course_postfixed(node.right, sequence)

        sequence.append(node)

        del node
        return sequence


    def get_root(self):
        return self.root
