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
    degree_count = [0 for i in range(n)]
    delta_length = []
    n_edges = 0
    initial_density = 0
    aux = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(l_edges[i])):
            extremity = l_edges[i][j]
            degree_count[extremity] += 1
            n_edges += 1
    for i in range(n):
        delta[degree_count[i]].append(i)
    for i in range(n):
        delta_length.append(len(delta[i]))
    for i in range(n):
        for j in range(len(delta[i])):
            aux[delta[i][j]] = [i, j]
    # divide by 2 times the number of vertices because each edge is counted twice as the graph is not oriented
    n_edges //= 2
    n_vertexes = g[0]
    densest = n_edges / g[0]
    return delta, delta_length, n_edges, n_vertexes, densest, aux, l_edges


def choose_min_degree(delta, position):
    while not delta[position]:
        position += 1
    return delta[position][0], position


def update_delta(delta, vertex, aux, l_edges, delta_length):
    # has to change for the last vertex
    edges_deleted = 0
    deg_selected, position_selected = aux[vertex]
    delta[deg_selected].pop(position_selected)
    delta_length[deg_selected] += -1
    for el in l_edges[vertex]:
        # we know that deg cannot be equal to 0
        (deg, position) = aux[el]
        print(delta)
        delta[deg].pop(position)
        print(delta)
        delta_length[deg] += -1
        delta[deg - 1].append(el)
        print('Delta:', delta)
        delta_length[deg - 1] += 1
        aux[el] = [deg - 1, delta_length[deg - 1]]
        edges_deleted += 1
    return delta, delta_length, edges_deleted


def densest_approximation(g):
    delta, delta_length,  n_edges, n_vertices, densest, aux, l_edges = initialize(
        g)
    h = g
    for i in range(n_vertices):
        v = choose_min_degree(delta, 0)
        delta, delta_length, edges_deleted = update_delta(
            delta, v[0], aux, l_edges, delta_length)
        n_edges -= edges_deleted
        n_vertices -= 1
        new_density = n_edges / n_vertices
        if new_density > densest:
            densest = new_density
            h = (n_vertices, )
