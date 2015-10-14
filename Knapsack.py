__author__ = 'antonio'

# Problema de la mochila resuelto por programacion dinamica (iterativa)
def ks(villains, time, cost_distance_1000 ):
    mem = [[0 for _ in xrange(time + 1)]
           for _ in xrange(len(villains) + 1)]

    grab = [[0 for _ in xrange(time + 1)]
            for _ in xrange(len(villains) + 1)]

    for i, villain in enumerate(villains, start=1):
        for j in xrange(1, time + 1):
            if villain.life <= j:
                if (villain.reward - cost_distance_1000 * (villain.distance/1000)) + mem[i][j - villain.life] >= mem[i - 1][j]:
                    mem[i][j] = (villain.reward - cost_distance_1000 * (villain.distance/1000)) + mem[i][j - villain.life]
                    grab[i][j] = 1
                else:
                    mem[i][j] = mem[i - 1][j]
            else:
                mem[i][j] = mem[i - 1][j]

    result = []
    n = len(villains)
    while n > 0 and time >= 0:
        if grab[n][time]:
            result.append(villains[n - 1])
            time -= villains[n - 1].life
        n -= 1
    return result
