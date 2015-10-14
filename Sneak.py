__author__ = 'antonio'


class Sneak:
    def __init__(self, name):
        self.name = name
        self.list_name_villains = []

    def __str__(self):
        return u'Chivato con nombre %s - Conoce el paradero de los villanos: ' % self.name + ', '.join(
            self.list_name_villains)
