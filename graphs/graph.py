class Graph:
    def __init__(self):
        self.graph = {}


    def add(self, node_a, node_b):
        if self.graph.has_key(node_a):
            self.graph[node_a].add(node_b)
        else:
            self.graph[node_a] = {node_b}


    def find_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if not self.graph.has_key(start):
            return None

        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath =  self.find_path(node, end, path)

                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath

        return shortest


    def bfs(self, start, end, path=[]):
        stack = [start]

        while stack:
            node = stack.pop()

            if not node in path:
                path = path + [node]
                stack = self.graph[node]

        return path


    def show_graph(self):
        for key in self.graph.keys():
            print '{}:'.format(key), ', '.join([element for element in self.graph[key]])
