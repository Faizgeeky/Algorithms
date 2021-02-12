

def Dij(nodes, distances,current):
  
    unvisited = {node: None for node in nodes} 
    visited = {}
    
    currentD = 0
    unvisited[current] = currentD

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                 continue
            nDist = currentD + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > nDist:
                unvisited[neighbour] = nDist
        visited[current] = currentD
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentD = sorted(candidates, key = lambda x: x[1])[0]

    print("\n\t ----- ",visited,"   ------\n")




nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 15, 'G': 1},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 5, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

Dij(nodes,distances,'B')


