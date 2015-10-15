__author__ = 'antonioirizar'


class Gui:
    def __init__(self, villains):
        self.name_days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        self.size_table = 20
        self.name_hours = 'Horas'
        self.villains = villains

    def generate_timetable(self):

        rows = []
        # create line
        line = ' '
        line += '-' * (((len(self.name_days) + 1) * self.size_table) + len(self.name_days))
        # create header
        header = '|' + self._cell(self.name_hours)
        for days in self.name_days:
            header += '|' + self._cell(days)
        header += '|'
        rows.append(line)
        rows.append(header)
        rows.append(line)
        # create table for villains
        cells = []
        for villain in self.villains:
            cotains_cell = villain.name + ' '
            for life in xrange(villain.life + 1, -1, -1):
                cells.append(self._cell(cotains_cell + 'vida ' + str(life)))

        # create rows for timetable
        for i in xrange(24):
            hours = '%i:00' % (i + 1)
            row = '|' + self._cell(hours)
            for j in xrange(7):
                try:
                    aux = self._cell(cells[(24 * j) + i])
                    row += '|' + aux
                except IndexError:
                    row += '|' + self._cell('Vacaciones')
            row += '|'
            rows.append(row)
            rows.append(line)
        return rows

    def _cell(self, name):
        size = self.size_table - len(name)
        if size % 2:
            size1 = size / 2 + 1
            size2 = size / 2
        else:
            size1 = size2 = size / 2
        return ' ' * size1 + name + ' ' * size2
