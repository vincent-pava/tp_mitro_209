from solution import densest_approximation
import snap

# Small scale examples
G1 = [[1, 2, 4, 5], [0, 2, 3, 4, 5], [0, 1, 4, 5], [1, 6, 7, 8, 9],
      [0, 1, 2, 5, 6], [0, 1, 2, 4], [3, 4], [3], [3], [3]]
G2 = [[1, 2], [0, 2], [1, 0]]
G3 = [[1, 2, 3], [0, 2], [0, 1, 3, 4], [0, 2], [2]]


print(densest_approximation(G1))
print(densest_approximation(G2))
print(densest_approximation(G3))
