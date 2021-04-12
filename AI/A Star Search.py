from collections import defaultdict
import sys

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.distance = defaultdict()

	# function to add an edge to graph
	def addEdge(self, src, dest, cost): 
		self.graph[src].append([dest, cost])

	def addval(self,city,cost):
		self.distance[city] = cost

	
	def Pqueue(self,city):
		self.queue = []
		
		dist = []
		for neighbor,cost in self.graph[city]:
			
			remaining = self.distance[neighbor]
			path = self.get_cost(city,neighbor)
			path+=self.path
			dist.append(path+remaining)
			# print(city,neighbor)
			# print(path,remaining,path+remaining)
		dist.sort()
		
		for cost in dist:
			self.queue.append(cost)

	# in graph dict see neighbors of given city and subtract the distance from the popped value and get_key() for that value
	# if key exists then its the right city
	def get_city(self,city,popped):
		for key,value in self.graph.items():
			for list1 in value:
				if key == city and self.get_key(popped-list1[1]-self.path)!="key doesn't exist":
					return list1[0]
		return "key doesn't exist"

	def DFSUtil(self, v, visited, goal):

		visited.add(v)
		print(v, end=' ')
		self.Pqueue(v)
		

		city = self.get_city(v,self.queue[0])
		self.path += self.distance[city]
		# print(v,city)
		# self.path+=self.get_cost(v,city)

		if city not in visited:
			if city != goal:
				self.DFSUtil(city, visited,goal)      #recursive function
			else:
				print(goal)
				sys.exit(0)
				
				

	def DFS(self, v,goal):
		visited = set()
		self.path=0
		self.DFSUtil(v, visited,goal)

	def get_key(self,val):
		for key, value in self.distance.items():
			if val == value:
				return key
		return "key doesn't exist"

	def get_cost(self,city,neighbor):
		
		for key, value in self.graph.items():
			
			for list1 in value:
				if key == city and  list1[0] == neighbor:
					return list1[1]
		return "key doesn't exist"

# Driver code
g = Graph()
g.addEdge("Oradea","Zerind",71)
g.addEdge("Oradea","Sibiu",151)
g.addEdge("Zerind","Arad",75)
g.addEdge("Zerind","Oradea",71)
g.addEdge("Arad","Zerind",75)
g.addEdge("Arad","Sibiu",140)
g.addEdge("Arad","Timisoara",118)
g.addEdge("Sibiu","Fagaras",99)
g.addEdge("Sibiu","Arad",140)
g.addEdge("Sibiu","Oradea",151)
g.addEdge("Sibiu","Rimnicu Vilcea",80)
g.addEdge("Timisoara","Arad",118)
g.addEdge("Timisoara","Lugoj",111)
g.addEdge("Lugoj","Timisoara",111)
g.addEdge("Lugoj","Mehadia",70)
g.addEdge("Mehadia","Lugoj",70)
g.addEdge("Mehadia","Dobreta",75)
g.addEdge("Dobreta","Mehadia",75)
g.addEdge("Dobreta","Craiova",120)
g.addEdge("Craiova","Dobreta",120)
g.addEdge("Craiova","Rimnicu Vilcea",146)
g.addEdge("Rimnicu Vilcea","Sibiu",80)
g.addEdge("Rimnicu Vilcea","Craiova",146)
g.addEdge("Rimnicu Vilcea","Pitesti",97)
g.addEdge("Pitesti","Rimnicu Vilcea",97)
g.addEdge("Pitesti","Craiova",138)
g.addEdge("Pitesti","Bucharest",101)
g.addEdge("Bucharest","Pitesti",101)
g.addEdge("Bucharest","Giurgu",90)
g.addEdge("Bucharest","Fagaras",211)
g.addEdge("Bucharest","Urziceni",85)
g.addEdge("Fagaras","Bucharest",211)
g.addEdge("Fagaras","Sibiu",99)
g.addEdge("Urziceni","Bucharest",85)
g.addEdge("Urziceni","Vaslui",142)
g.addEdge("Urziceni","Hirsova",98)
g.addEdge("Vaslui","Urziceni",142)
g.addEdge("Vaslui","Lasi",92)
g.addEdge("Lasi","Vaslui",892)
g.addEdge("Lasi","Neamt",87)
g.addEdge("Neamt","Lasi",87)
g.addEdge("Giurgiu","Bucharest",90)
g.addEdge("Hirsova","Urziceni",98)
g.addEdge("Hirsova","Eforie",86)
g.addEdge("Eforie","Hirsova",86)
g.addval("Arad",366)
g.addval("Bucharest",0)
g.addval("Craiova",160)
g.addval("Dobreta",242)
g.addval("Eforie",161)
g.addval("Fagaras",176)
g.addval("Giurgiu",77)
g.addval("Hirsova",151)
g.addval("lasi",226)
g.addval("Lugoj",244)
g.addval("Mehadia",241)
g.addval("Neamt",234)
g.addval("Oradea",380)
g.addval("Pitesti",101)
g.addval("Rimnicu Vilcea",193)
g.addval("Sibiu",253)
g.addval("Timisoara",329)
g.addval("Urziceni",80)
g.addval("Vaslui",199)
g.addval("Zerind",374)

print("Following is DFS from (starting from vertex 2)")
g.DFS("Arad","Bucharest")
