class Example(object):
    def __init__(self):
        self._x = 100

    @property
    def x(self):
        """
        I am the 'x' property
        :return: x
        """
        print('getter of x called')
        return self._x

    @x.setter
    def x(self, value):
        print('setter of x called')
        self._x = value

    @x.deleter
    def x(self):
        print('deleter of x called')
        del self._x

    def __str__(self):
        """
        return a string representation of the object Example
        """
        return str(self.x)


# noinspection PyStatementEffect
def run():
    """
    Run arbitrary instructions
    """
    example1 = Example()
    print(example1.x)
    example1.x = 50
    print(example1)
    del example1.x

run()
