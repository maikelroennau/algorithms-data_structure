from binary_tree import BinaryTree


if __name__ == '__main__':
    tree = BinaryTree()

    values = [9, 6, 4, 3, 1, 8, 2, 5, 0, 7]

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
