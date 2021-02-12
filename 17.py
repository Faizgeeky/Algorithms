from collections import defaultdict

#Class to represent a graph
class Graph:

	def __init__(self, vertices):
		self.V = vertices

	def printSolution(self, reach):
		for i in range(self.V):
			for j in range(self.V):
				if (i == j):
				    print("%d\t" % (1))
				else:
				    print("%d\t" %(reach[i][j]))
           
			
	
	
	def tClo(self,graph):
		reach =[i[:] for i in graph]
		
		for k in range(self.V):
			
			# Pick all vertices as source one by one
			for i in range(self.V):
				
				
				for j in range(self.V):

					reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

		self.printSolution(reach)
		
g= Graph(4)

graph = [[1, 1, 0, 1],
		[0, 1, 1, 0],
		[0, 0, 1, 1],
		[0, 0, 0, 1]]

#Print the solution
g.tClo(graph)
