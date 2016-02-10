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
def run_example():
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


# run_example()


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
        if not self.birthday:
            return ''
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
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age


def run_person():
    qazi = Person('Bob')
    print(qazi.name)
    qazi.name = 'Qazi'
    qazi.birthday = datetime.date(1994, 7, 14)
    print(qazi.birthday)
    print(qazi)
    print('Age in days:', qazi.age)
    print(qazi)
    john = Person('John')
    john.birthday = datetime.date(1995, 10, 21)
    print(qazi > john)
    # assert qazi < john is not True
    assert (qazi > john) is True  # __gt__
    assert (qazi != john) is True  # __ne__
    assert (qazi < john) is False  # __lt__
    assert (qazi == john) is False  # __eq__


# run_person()


# Inheritance
class MITPerson(Person):
    next_id_num = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self._id_num = MITPerson.next_id_num
        MITPerson.next_id_num += 1

    @property
    def id_num(self):
        return self._id_num

    def __lt__(self, other):
        return self.id_num < other.id_num

    def is_student(self):
        return type(self) == UG or type == G


def run_mit_person():
    qazi = Person('Qazi')
    qazi.birthday = datetime.date(1994, 7, 14)
    qazi_mit = MITPerson(qazi)
    print(qazi_mit)
    john = Person('john')
    john.birthday = datetime.date(1995, 7, 14)
    john_mit = MITPerson(john)
    assert qazi_mit.id_num < john_mit.id_num
    print(qazi_mit.id_num)
    print(john_mit.id_num)
    print(Person.__lt__(qazi_mit, john_mit))
    print(Person.__lt__(john_mit, qazi_mit))


# run_mit_person()


class UG(MITPerson):
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self._year = None

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, the_year):
        if the_year > 5:
            raise OverflowError('Too Many Years!')
        self._year = the_year

    def __str__(self):
        return Person.__str__(self) + ' ' + '\nundergrad year: ' + str(self.year)


class G(MITPerson):
    pass


def run_ug_person():
    qazi = Person('qazi')
    qazi.birthday = datetime.date(1994, 7, 14)
    qazi_mit = MITPerson(qazi)
    qazi_ug = UG(qazi_mit)
    print(qazi_ug.year)
    qazi_ug.year = 4
    print(qazi_ug)
    print(qazi_ug.is_student())
    assert qazi_ug.is_student() is True
    john = Person('john')
    john.birthday = datetime.date(1995, 10, 15)
    john_mit = MITPerson(john)
    assert john_mit.is_student() is False

run_ug_person()