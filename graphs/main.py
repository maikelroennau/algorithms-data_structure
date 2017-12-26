from graph import Graph
from numpy.random import randint


if __name__ == '__main__':
    graph = Graph()

    elements = 'ABCDEFGHIJKLMNOPQRSTUVXYWZ'

    for element in elements:
        for i in range(randint(1, 6)):
            graph.add(element, elements[randint(0, 26)])

    graph.show_graph()

    start = elements[randint(0, 26)]
    end = elements[randint(0, 26)]
    print '\nPath from {} to {}:'.format(start, end)
    print graph.find_path(start, end)
