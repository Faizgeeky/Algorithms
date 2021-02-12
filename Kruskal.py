class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.Graph = []

    def add_e(self, u, v, w):
        self.Graph.append([u, v, w])

    # Search 

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #   Kruskal alGorithm
    def kruskal_alGo(self):
        result = []
        i, e = 0, 0
        self.Graph = sorted(self.Graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.Graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weiGht in result:
            print("%d - %d: %d" % (u, v, weiGht))


G = Graph(6)
G.add_e(0, 1, 4)
G.add_e(0, 2, 4)
G.add_e(1, 2, 2)
G.add_e(1, 0, 4)
G.add_e(2, 0, 4)
G.add_e(2, 1, 2)
G.add_e(2, 3, 3)
G.add_e(2, 5, 2)
G.add_e(2, 4, 4)
G.add_e(3, 2, 3)
G.add_e(3, 4, 3)
G.add_e(4, 2, 4)
G.add_e(4, 3, 3)
G.add_e(5, 2, 2)
G.add_e(5, 4, 3)
G.kruskal_alGo()
