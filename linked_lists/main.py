from doubly_linked_list import DoublyLinkedList
from singly_linked_list import SinglyLinkedList


if __name__ == '__main__':
    first = 0
    middle = 50000
    last = 100000

    print 'Running doubly linked list'
    doubly_linked_list = DoublyLinkedList()

    [doubly_linked_list.add(x) for x in range(last)]

    doubly_linked_list.remove(first)
    doubly_linked_list.remove(middle)
    doubly_linked_list.remove(last-1)
    doubly_linked_list.remove(-1)

    print '\nRunning singly linked list'
    singly_linked_list = SinglyLinkedList()
    [singly_linked_list.add(x) for x in range(last)]

    singly_linked_list.remove(first)
    singly_linked_list.remove(middle)
    singly_linked_list.remove(last-1)
    singly_linked_list.remove(-1)
