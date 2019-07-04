# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

print("\n------------------------------ De A a B ------------------------------\n")

print("Búsqueda en anchura: ", end="")
print(search.breadth_first_graph_search(ab).path())

print("Búsqueda en profundidad: ", end="")
print(search.depth_first_graph_search(ab).path())

print("Búsqueda de ramificación y acotación: ", end="")
print(search.branch_and_bound_graph_search(ab).path())

print("Búsqueda de ramificación y acotación con subestimación: ", end="")
print(search.branch_and_bound_with_understimates_graph_search(ab).path())

# Result:

# [<Node B>, <Node F>, <Node S>, <Node A>] : 140 + 99 + 211 = 450
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 118 + 111 + 70 + 75 + 120 + 138 + 101 = 733
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 140 + 80 + 97 + 101 = 418
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 140 + 80 + 97 + 101 = 418

tr = search.GPSProblem('T', 'R', search.romania)

print("\n------------------------------ De T a R ------------------------------\n")

print("Búsqueda en anchura: ", end="")
print(search.breadth_first_graph_search(tr).path())

print("Búsqueda en profundidad: ", end="")
print(search.depth_first_graph_search(tr).path())

print("Búsqueda de ramificación y acotación: ", end="")
print(search.branch_and_bound_graph_search(tr).path())

print("Búsqueda de ramificación y acotación con subestimación: ", end="")
print(search.branch_and_bound_with_understimates_graph_search(tr).path())

# Result

# [<Node R>, <Node S>, <Node A>, <Node T>] : 118 + 140 + 80 = 338
# [<Node R>, <Node S>, <Node F>, <Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>] : 111 + 70 + 75 + 120 + 138 + 101 + 211 + 99 + 80 = 1005
# [<Node R>, <Node S>, <Node A>, <Node T>] : 118 + 140 + 80 = 338
# [<Node R>, <Node S>, <Node A>, <Node T>] : 118 + 140 + 80 = 338

# Cambiar para probar otras ciudades

city_1 = 'O'
city_2 = 'C'

print("\n------------------------------ De " + city_1 + " a " + city_2 + " ------------------------------\n")

other = search.GPSProblem(city_1, city_2, search.romania)

print("Búsqueda en anchura: ", end="")
print(search.breadth_first_graph_search(other).path())

print("Búsqueda en profundidad: ", end="")
print(search.depth_first_graph_search(other).path())

print("Búsqueda de ramificación y acotación: ", end="")
print(search.branch_and_bound_graph_search(other).path())

print("Búsqueda de ramificación y acotación con subestimación: ", end="")
print(search.branch_and_bound_with_understimates_graph_search(other).path())
