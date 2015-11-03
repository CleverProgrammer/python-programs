"""
recursive class definition for a non-empty list of nodes
"""


class Increment(object):

    def __init__(self, count):
        self.count = count

    def incrementer(self):
        self.count += 1


class NodeList:
    """
    basic class definition for non-empty lists using recursion
    """

    def __init__(self, value):
        """
        create a list with one node
        """

        self._value = value
        self._next = None

    def append(self, value):
        """
        append a node to an existing list of nodes
        """
        counter.incrementer()
        if self._next is None:
            new_node = NodeList(value)
            self._next = new_node
        else:
            self._next.append(value)

    def __str__(self):
        """
        Build standard string representation for a list
        """
        if self._next is None:
            return '[' + str(self._value) + ']'
        else:
            rest_str = str(self._next)
            rest_str = rest_str[1:]
            return '[' + str(self._value) + ", " + rest_str


node_list = NodeList(2)
counter = Increment(0)
# TRIANGLE NUMBERS
# .5*n(n+1)
node_list.append(3)  # 1         +1
node_list.append(4)  # 3         +2
node_list.append(4)  # 6         +3
node_list.append(4)  # 10        +4
node_list.append(4)  # 15        +5
node_list.append(4)  # 21        +6
node_list.append(4)  # 28        +7
node_list.append(4)  # 36        +8
node_list.append(4)  # 45        +9
node_list.append(4)  # 55        +10
print(counter.count)
print(node_list)
