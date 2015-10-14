__author__ = 'antonio'

from random import randint


class Villain:
    def __init__(self, name):
        self.name = name
        self.life = randint(5, 40)
        self.distance = randint(0, 5000)
        self.reward = randint(1, 100)
        self.is_sneak = randint(0, 1)
        if self.is_sneak:
            self.list_name_villains = []

    def __str__(self):
        return u'%s - Tiene %i puntos de vida - Se encuentra a una distancia de %i - Recompensa de %i euros.' % (
            self.name, self.life, self.distance, self.reward)
