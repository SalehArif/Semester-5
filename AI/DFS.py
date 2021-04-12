# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
 
 
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.list = ["Arad","Sibiu","Timisoara","Fagaras","Bucharest","Zerind","Oradea","Lugoj","Mehadia","Dobreta","Craiova", "Rimnicu Vilcea","Pitesti","Urziceni","Vaslui","Lasi","Neamt","Giurgiu","Hirsova","Eforie"]
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        src = self.index(u)
        dest = self.index(v)
        self.graph[src].append(dest)
 
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(self.list[v], end=' ')
        
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if self.goal(visited):
                return
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, city):
 
        # Create a set to store visited vertices
        visited = set()
        ind = self.index(city)
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(ind, visited)

    def index(self, city):
        for i in range(len(self.list)):
            if self.list[i]==city:
                return i

    def goal(self, visited):
        # self.goal = 
        ind = self.index("Bucharest")
        if ind in visited:
            return True
        return False

 
# Driver code
 
 
# Create a graph given
# in the above diagram
g = Graph()
g.addEdge("Oradea","Zerind")
g.addEdge("Oradea","Sibiu")
g.addEdge("Zerind","Oradea")
g.addEdge("Zerind","Arad")
g.addEdge("Arad", "Zerind")
g.addEdge("Arad", "Sibiu")
g.addEdge("Arad", "Timisoara")
g.addEdge("Sibiu","Fagaras")
g.addEdge("Sibiu","Arad")
g.addEdge("Sibiu","Oradea")
g.addEdge("Sibiu","Rimnicu Vilcea")
g.addEdge("Timisoara","Arad")
g.addEdge("Timisoara","Lugoj")
g.addEdge("Lugoj","Timisoara")
g.addEdge("Lugoj","Mehadia")
g.addEdge("Mehadia","Lugoj")
g.addEdge("Mehadia","Dobreta")
g.addEdge("Dobreta","Mehadia")
g.addEdge("Dobreta","Craiova")
g.addEdge("Craiova","Dobreta")
g.addEdge("Craiova","Rimnicu Vilcea")
g.addEdge("Rimnicu Vilcea","Sibiu")
g.addEdge("Rimnicu Vilcea","Craiova")
g.addEdge("Rimnicu Vilcea","Pitesti")
g.addEdge("Pitesti","Rimnicu Vilcea")
g.addEdge("Pitesti","Craiova")
g.addEdge("Bucharest","Pitesti")
g.addEdge("Bucharest","Giurgu")
g.addEdge("Bucharest","Fagaras")
g.addEdge("Bucharest","Urziceni")
g.addEdge("Fagaras","Bucharest")
g.addEdge("Fagaras","Sibiu")
g.addEdge("Urziceni","Bucharest")
g.addEdge("Urziceni","Vaslui")
g.addEdge("Urziceni","Hirsova")
g.addEdge("Vaslui","Urziceni")
g.addEdge("Vaslui","Lasi")
g.addEdge("Lasi","Vaslui")
g.addEdge("Lasi","Neamt")
g.addEdge("Neamt","Lasi")
g.addEdge("Giurgiu","Bucharest")
g.addEdge("Hirsova","Urziceni")
g.addEdge("Hirsova","Eforie")
g.addEdge("Eforie","Hirsova")

 
print("Following is DFS from (starting from vertex Arad)")
g.DFS("Arad")
print()