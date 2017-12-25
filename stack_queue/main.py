from stack import Stack
from queue import Queue


if __name__ == '__main__':
    print 'Stack'
    stack = Stack()
    
    name = 'uannoR leicaM lekiaM'
    [stack.push(x) for x in name]

    for x in name:
        print stack.pop().data,

    print
    print '\nQueue'
    queue = Queue()

    name = 'Maikel Maciel Ronnau'
    [queue.add(x) for x in name]

    for x in name:
        print queue.remove().data,
