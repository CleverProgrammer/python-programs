class Character(object):
    def __init__(self,name):
        self.health = 100
        self.name = name
    def printName(self):
        print self.name

class Blacksmith(Character):
    def __init__(self,name,forgeName):
        super(Blacksmith,self).__init__(name)
        self.forge = Forge(ForgeName)


bs = Blacksmith("Murg")
print Blacksmith.printName
print bs.health

class Maid(Character):
    def __init__(self):
        self.health = 40

maid = Maid()
print maid.health


