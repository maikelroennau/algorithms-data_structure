from binary_tree import BinaryTree


if __name__ == '__main__':
    tree = BinaryTree()

    values = [5, 3, 2, 4, 7, 6, 8]

    #        5
    #      /   \
    #     3     7
    #    / \   / \
    #   2   4 6   8

    [tree.add(x) for x in values]

    print 'Input:',
    print ', '.join(str(x) for x in values)


    print '\nPrefixed.:',
    for node in tree.course_prefixed():
        print node.data,

    print
    print '\nInfixed..:',
    for node in tree.course_infixed():
        print node.data,

    print
    print '\nPostfixed:',
    for node in tree.course_postfixed():
        print node.data,


    print
    print '\nSearch:',
    print ', '.join(str(x) for x in values)
    for x in values:
        result = tree.search(x)
        if result:
            print result.data,
        else:
            print None,

    result = None

    print
    print '\nSearch:',
    print ', '.join(str(x * -1) for x in values)
    for x in values:
        result = tree.search(x * -1)
        if result:
            print result.data,
        else:
            print None,


    print
    print '\nRemove: 5 (root)'
    tree.remove(5)
    print 'Result:',
    for node in tree.course_infixed():
        print node.data,

    print
    print '\nRemove: 4'
    tree.remove(4)
    print 'Result:',
    for node in tree.course_infixed():
        print node.data,

    print
    print '\nRemove: 8'
    tree.remove(8)
    print 'Result:',
    for node in tree.course_infixed():
        print node.data,
