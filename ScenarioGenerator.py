__author__ = 'antonio'

from random import randint, choice
from Villain import Villain
from Sneak import Sneak
from Knapsack import ks


class ScenarioGenerator:
    def __init__(self):

        self._cost_distance_1000 = randint(1, 10)
        villains = []
        self.sneaks = []
        self.villains_to_kill = []
        self.reward = None

        # generate villains
        for i in xrange(randint(5, 15)):
            villain = Villain(u'villano %i' % i)
            if villain.is_sneak:
                self.sneaks.append(villain)
            villains.append(villain)

        # generate sneaks
        for i in xrange(randint(1, 8)):
            self.sneaks.append(Sneak(u'chivato %i' % i))

        # put villains in list of sneak
        for villain in villains:
            sneak = choice(self.sneaks)
            sneak.list_name_villains.append(villain)

    def calculate_schedule(self):
        # get all villains and
        villains = []
        for sneak in self.sneaks:
            for villain in sneak.list_name_villains:
                if not villain.is_sneak:
                    villains.append(villain)

        time = 7 * 24
        self.villains_to_kill, self.reward= ks(villains, time, self._cost_distance_1000)

import pprint
a = ScenarioGenerator()
a.calculate_schedule()
print a.sneaks
print a._cost_distance_1000
for i in a.villains_to_kill:

    print(i)
print a.reward