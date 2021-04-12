# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.list = ["Arad","Sibiu","Timisoara","Fagaras","Bucharest","Zerind","Oradea","Lugoj","Mehadia","Dobreta","Craiova", "Rimnicu Vilcea","Pitesti","Urziceni","Vaslui","Lasi","Neamt","Giurgiu","Hirsova","Eforie"]
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        src = self.index(u)
        dest = self.index(v)
        self.graph[src].append(dest)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (len(self.list) + 1)
        ind = self.index(s)
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as 
        # visited and enqueue it
        queue.append(ind)
        visited[ind] = True
 
        while queue:
 
            # Dequeue a vertex from 
            # queue and print it
            ind = queue.pop(0)
            print (self.list[ind], end = " ")
            if self.goal(self.list[ind]):
                return
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[ind]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def index(self, city):
        for i in range(len(self.list)):
            if self.list[i]==city:
                return i

    
    def goal(self,i):
        if(i=="Bucharest"):
            return True
        return False

# Driver code
 
# Create a graph given in
# the above diagram
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

print ("Following is Breadth First Traversal (starting from vertex Arad)")
g.BFS("Arad")