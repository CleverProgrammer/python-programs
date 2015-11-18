import datetime


class Example(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        """
        I am the 'x' property
        :return: x
        """
        print('getter of x called')
        return self._x

    @property
    def y(self):
        """
        I am the 'y' property
        :return: y
        """
        print('getter of y called')
        return self._y

    @x.setter
    def x(self, value):
        print('setter of x called')
        self._x = value

    @y.setter
    def y(self, value):
        print('setter of y called')
        self._y = value

    @x.deleter
    def x(self):
        print('deleter of x called')
        del self._x

    @y.deleter
    def y(self):
        print('deleter of y called')
        del self._y

    def __str__(self):
        """
        return a string representation of the object Example
        """
        return str(self.x) + ' ' + str(self.y)


# noinspection PyStatementEffect
def run():
    """
    Run arbitrary instructions
    """
    example1 = Example(10, 20)
    print(example1.x)
    print(example1.y)
    example1.x = 50
    example1.y = 60
    print(example1)
    del example1.x
    del example1.y


run()


class Person(object):
    def __init__(self, name):
        self._name = name
        self._birthday = None

    @property
    def name(self):
        return self._name

    @property
    def birthday(self):
        return self._birthday

    @property
    def age(self):
        assert self.birthday is not None
        return (datetime.date.today() - self.birthday).days

    @name.setter
    def name(self, name):
        self._name = name

    @birthday.setter
    def birthday(self, birth_date):
        assert isinstance(birth_date, datetime.date)
        self._birthday = birth_date

    def __str__(self):
        person_description = '\n\nName: ' + \
                             str(self.name) + '\n' \
                                              'Birthday: ' + \
                             str(self.birthday) + '\n' \
                                                  'Age in days: ' + str(self.age)
        return person_description

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name


def run2():
    qazi = Person('Bob')
    print(qazi.name)
    qazi.name = 'Qazi'
    qazi.birthday = datetime.date(1994, 7, 14)
    print(qazi.birthday)
    print(qazi)
    print('Age in days:', qazi.age)
    print(qazi)
    john = Person('John')
    print(qazi > john)
    # assert qazi < john is not True
    assert qazi > john  # __gt__
    assert qazi != john  # __ne__
    assert not qazi < john  # __lt__
    assert not qazi == john  # __eq__
run2()
