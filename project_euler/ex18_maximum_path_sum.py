"""

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

import weakref


class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    def __repr__(self):
        return f'nó({self._value})'

    def __iter__(self):
        return iter(self._children)

    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self._children.append(child)
        child.parent = self

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()



def test_node():
    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    root.add_child(c1)
    root.add_child(c2)
    c1.add_child(Node(3))
    c1.add_child(Node(4))
    c2.add_child(Node(5))

    expected = (
        'nó(0)',
        'nó(1)',
        'nó(3)',
        'nó(4)',
        'nó(2)',
        'nó(5)'
    )
    for i, c in enumerate(root.depth_first()):
        assert repr(c) == expected[i]


test_node()


def calc_clindren(node, level):
    c1 = node*(2-1) + level
    c2 = node*(2-1) + level + 1
    return node, (c1, c2)


def test_calc_clindren():
    assert calc_clindren(1, 1) == (1, (2, 3))
    assert calc_clindren(2, 2) == (2, (4, 5))
    assert calc_clindren(3, 2) == (3, (5, 6))
    assert calc_clindren(4, 3) == (4, (7, 8))
    assert calc_clindren(5, 3) == (5, (8, 9))
    assert calc_clindren(6, 3) == (6, (9, 10))


test_calc_clindren()


nodes = list()


with open('ex18_data.txt') as file:
    for level, line in enumerate(file, 1):
        for node in line.strip().split(' '):
            node = int(node)
            n = Node(node)
            for child in calc_clindren(node, level)[1]:
                n.add_child(Node(child))
            nodes.append(n)


for node in nodes:
    print(node, node.parent)

# for i in  reversed(piramid):
#     print(i)


# print(calc_n(5, 3))