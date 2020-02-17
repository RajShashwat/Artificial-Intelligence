#Coded By Shashwat Raj
#A program for BFS Traversal

from collections import defaultdict

#Class to manage Graph
class Graph:
    
    #Constructor
    def __init__(self):
        self.graph= defaultdict(list)
    
    #Adding Edges of graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    #BFS Traversal
    def bfs(self, node):
        visited = []   #List to keep track of visited nodes.
        queue = []     
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

#Input of Graph Nodes
edges=input("Enter the edges using space: ").split()
g=Graph()
for edge in edges:
    g.addEdge(edge[:1],edge[1:])
    
# Driver Code
g.bfs(input("Enter the starting node: "))