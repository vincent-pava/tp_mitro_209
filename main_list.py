import snap
l_edges = [[1, 2, 4, 5], [0, 2, 3, 4, 5], [0, 1, 4, 5], [1, 6, 7, 8, 9],
           [0, 1, 2, 5, 6], [0, 1, 2, 4], [3, 4], [3], [3], [3]]
G1 = (10, l_edges)


def initialize(g):
    '''This function initializes the different data structures used in the algorithm
    delta = list of lists containing the vertices of a certain degree
    l_delta = list of the lengths of the lists in delta
    aux = list with for each vertex [deg, position] where deg is its current degree and position is its position in the degree list in delta'''
    l_edges = g[1]
    n = g[0]
    delta = [[] for i in range(n)]
    degree = [0 for i in range(n)]
    delta_length = []
    n_edges = 0
    initial_density = 0
    aux = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(l_edges[i])):
            extremity = l_edges[i][j]
            degree[extremity] += 1
            n_edges += 1
    for i in range(n):
        delta[degree[i]].append(i)
    for i in range(n):
        delta_length.append(len(delta[i]))
    for i in range(n):
        for j in range(len(delta[i])):
            aux[delta[i][j]] = [i, j]
    # divide by 2 times the number of vertices because each edge is counted twice as the graph is not oriented
    initial_density = n_edges / (2 * g[0])
    return delta, delta_length, initial_density, aux


print(initialize(G1))
