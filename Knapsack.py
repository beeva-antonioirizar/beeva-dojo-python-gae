__author__ = 'antonio'

# Problema de la mochila resuelto por programacion dinamica (iterativa)
def ks(villains, weight):
    mem = [[0 for j in xrange(weight + 1)]
           for i in xrange(len(villains) + 1)]

    grab = [[0 for j in xrange(weight + 1)]
           for i in xrange(len(villains) + 1)]

    for i, item in enumerate(villains, start=1):
        for j in xrange(1, weight + 1):
            if item.weight <= j:
                if item.value + mem[i][j - item.weight] >= mem[i - 1][j]:
                    mem[i][j] = item.value + mem[i][j - item.weight]
                    grab[i][j] = 1
                else:
                    mem[i][j] = mem[i - 1][j]
            else:
                mem[i][j] = mem[i - 1][j]

    itemList = []
    n = len(villains)
    while n > 0 and weight >= 0:
        if grab[n][weight]:
            itemList.append(villains[n-1])
            weight -= villains[n-1].weight
        n -= 1
    return itemList

print ks(items, 15)