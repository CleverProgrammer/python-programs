__author__ = 'Rafeh'


class StreetFighter:
    def __init__(self, name, health):
        self.health = health
        self.name = name

    def get_attacked(self):
        self.health -= 2
        print('ouch')
        if self.health < 1:
            print('I got DEAD!')

    def heal(self):
        if self.health > 99:
            print(self.health)
            print('cant heal no more sir, already at full!')
        elif self.health == 99:
            self.health += 1
            print(self.health)
            print('oh yeah, healing myself tasted good')
            print('health at max')
        else:
            self.health += 2
            print(self.health)
            print('oh yeah, healing myself tasted good')

    def attack(self, fighter):
        if fighter:
            fighter.get_attacked()
            print('How did that feel', str(fighter.name))
            print(fighter.health)
