#Coded By Shashwat Raj
#A program for DFS Traversal

from collections import defaultdict

#Class to manage Graph
class Graph:
    
    #Constructor
    def __init__(self):
        self.graph= defaultdict(list)
     
    #Adding Edges of graph    
    def addEdge(self,u,v):
        self.graph[u].append(v)
     
    #A function used by DFS     
    def dfsutil(self,visited, node):
        
        if node not in visited:
            print (node, end=" ")
            visited.append(node)
            for neighbour in self.graph[node]:
                self.dfsutil(visited, neighbour)
    #DFS Function 
    def dfs(self,node):
        visited = [] # Array to keep track of visited nodes
        self.dfsutil(visited,node)

#Input of Graph Nodes
edges=input("Enter the edges using space: ").split()
g=Graph()
for edge in edges:
    g.addEdge(edge[:1],edge[1:])
    
# Driver Code
g.dfs(input("Enter the starting node: "))