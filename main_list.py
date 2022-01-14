import snap
l_edges = [[1, 2, 4, 5], [0, 2, 3, 4, 5], [0, 1, 4, 5], [1, 6, 7, 8, 9],
           [0, 1, 2, 5, 6], [0, 1, 2, 4], [3, 4], [3], [3], [3]]
G1 = (10, l_edges)


def initialize(g):
    l_edges = g[1]
    n = g[0]
    delta = [[] for i in range(g[0])]
    degree = [0 for i in range(g[0])]
    n_vertices = 0
    for i in range(g[0]):
        for j in range(len(l_edges[i])):
            extremity = l_edges[i][j]
            degree[extremity] += 1
            n_vertices += 1
    for i in range(n):
        delta[degree[i]].append(i)
