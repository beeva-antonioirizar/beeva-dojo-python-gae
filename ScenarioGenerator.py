__author__ = 'antonio'

from random import randint
from villain import Villain

class ScenarioGenerator:

    def __init__(self):

        self.villains = []
        self.sneak = []
        # generate villains
        for i in xrange(randint(5, 15)):
            villain = Villain(u'villano %i' %i)
            if villain.is_sneak:
                self.sneak.append(villain)
            else:
                self.villains.append(villain)
        self._distance
