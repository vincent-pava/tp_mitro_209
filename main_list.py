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


def choose_min_degree(delta, index):
    while not delta[index]:
        index += 1
    return delta[index][-1], index


def update_delta(delta, vertex, aux, l_edges, delta_length, kept_vertices):
    # has to change for the last vertex
    edges_deleted = 0
    deg_selected, position_selected = aux[vertex]
    delta[deg_selected][position_selected], delta[deg_selected][-1] = delta[deg_selected][position_selected], delta[deg_selected][-1]
    aux[delta[deg_selected][position_selected]] = [
        deg_selected, position_selected]
    vertex_deleted = delta[deg_selected].pop()
    delta_length[deg_selected] += -1
    for el in l_edges[vertex]:
        if kept_vertices[el]:
            # we know that deg cannot be equal to 0 because otherwise we don't enter the loop
            (deg, position) = aux[el]
            delta[deg][position], delta[deg][-1] = delta[deg][-1], delta[deg][position]
            aux[delta[deg][position]] = [deg, position]
            delta[deg].pop()
            delta_length[deg] += -1
            delta[deg - 1].append(el)
            delta_length[deg - 1] += 1
            aux[el] = [deg - 1, delta_length[deg - 1] - 1]
            edges_deleted += 1
    kept_vertices[vertex] = False
    return delta, delta_length, edges_deleted, kept_vertices


def densest_approximation(g):
    delta, delta_length,  n_edges, n, densest, aux, l_edges = initialize(
        g)
    n_vertices = n
    kept_vertices = [True for i in range(n)]
    h = kept_vertices
    index = 0
    for i in range(n-1):
        v, index = choose_min_degree(delta, index)
        index -= 1
        delta, delta_length, edges_deleted, kept_vertices = update_delta(
            delta, v, aux, l_edges, delta_length, kept_vertices)
        tab = kept_vertices.copy()
        n_edges -= edges_deleted
        n_vertices -= 1
        new_density = n_edges / n_vertices
        print(new_density, densest)
        if new_density > densest:
            densest = new_density
            h = tab
    return rebuild_graph(h, l_edges, n)


def rebuild_graph(bool_tab, l_edges, n):
    new_l_edges = [[] for i in range(n)]
    for i in range(n):
        if bool_tab[i]:
            k = len(l_edges[i])
            for j in range(k):
                if bool_tab[l_edges[i][j]]:
                    new_l_edges[i].append(l_edges[i][j])
    return new_l_edges


print(densest_approximation(G1))
