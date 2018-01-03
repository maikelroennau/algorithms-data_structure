from numpy.random import randint
import time


def insertion_sort(vector):
    for i in range(1, len(vector)):
        k = i
        current_value = vector[i]

        while k > 0 and vector[k-1] > current_value:
            vector[k] = vector[k-1]
            k -= 1

        vector[k] = current_value


def bubble_sort(vector):
    sortings = True

    while sortings:
        sortings = False

        for i in range(len(vector)-1):
            if vector[i] > vector[i+1]:
                aux = vector[i]
                vector[i] = vector[i+1]
                vector[i+1] = aux
                sortings = True


def selection_sort(vector):
    for i in range(len(vector)-1):
        smallest = i+1
        for j in range(i+1, len(vector)):
            if vector[j] < vector[smallest]:
                smallest = j

        aux = vector[i]
        vector[i] = vector[smallest]
        vector[smallest] = aux


def show_vector(vector):
    print 'Subject vector: \n\t',
    for i in range(len(vector)):
        if i > 0 and i % 10 == 0:
            print '\n\t',
        print '{0:0=2d}'.format(vector[i]),


def show_sample(vector):
    return ', '.join('{0:0=2d}'.format(x) for x in vector[:10]) + ', ...'


if __name__ == '__main__':
    elements = 100
    unsorted_vector = [randint(0, 100) for x in range(elements)]

    show_vector(unsorted_vector)

    insertion_vector = unsorted_vector[:]
    bubble_vector = unsorted_vector[:]
    selection_vector = unsorted_vector[:]

    start = time.time()
    insertion_sort(insertion_vector)
    end = time.time()
    print '\n\nInsertion sort'
    print '\tElements:', elements
    print '\tSorted sample:', show_sample(insertion_vector)
    print '\tTime....: {} second(s)'.format(round(end - start, 10))


    start = time.time()
    bubble_sort(bubble_vector)
    end = time.time()
    print '\nBubble sort'
    print '\tElements:', elements
    print '\tSorted sample:', show_sample(bubble_vector)
    print '\tTime....: {} second(s)'.format(round(end - start, 10))

    start = time.time()
    bubble_sort(selection_vector)
    end = time.time()
    print '\nSelection sort'
    print '\tElements:', elements
    print '\tSorted sample:', show_sample(selection_vector)
    print '\tTime....: {} second(s)'.format(round(end - start, 10))