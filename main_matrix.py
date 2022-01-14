import snap

mat1 = [[0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
g1 = [10, mat1]


def initialize(g):
    n = g[0]
    mat = g[1]
    delta = [[] for i in range(n)]
    n_vertexes = 0
    for i in range(n):
        degree = 0
        for j in range(n):
            if mat[i][j] == 1:
                degree += 1
                n_vertexes += 1
        delta[degree - 1].append(i)
    n_vertexes = n_vertexes/2
    density = (n_vertexes/n)
    h = g
    return g, h, n_vertexes, density, delta


def update(g, h, n_vertexes, density, delta):
    n = g[0]
    mat = g[1]
    i = 0
    deleted = 0
    while (not delta[i]):
        i += 1
    v = delta[i][0]
    del delta[i][0]
    for j in range(n):
        if mat[v][j] == 1:
            deleted += 1
    for j in range(n):
        del mat[j][v]
    del mat[v]
    g[0] += -1
    new_density = (n_vertexes-deleted)/(n-1)
    new_delta = delta
    if (density < new_density):
        h = g
    return g, h, (n_vertexes-deleted), new_density, new_delta


init = initialize(g1)


def subset(g):
    g, h, n_vertexes, density, delta = initialize(g)
    while(g[0] != 0):
        g, h, n_vertexes, density, delta = update(
            g, h, n_vertexes, density, delta)
    return h


print(subset(g1))
