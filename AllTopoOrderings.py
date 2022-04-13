# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # stores in-degree of a vertex
        # initialize in-degree of each vertex by 0
        self.indegree = [0] * n
 
        # add edges to the directed graph
        for (src, dest) in edges:
 
            # add an edge from source to destination
            self.adjList[src].append(dest)
 
            # increment in-degree of destination vertex by 1
            self.indegree[dest] = self.indegree[dest] + 1
 
 
# Recursive function to find all topological orderings of a given DAG
def findAllTopologicalOrderings(graph, path, discovered, n):
 
    # do for every vertex
    for v in range(n):
 
        # proceed only if the current node's in-degree is 0 and
        # the current node is not processed yet
        if graph.indegree[v] == 0 and not discovered[v]:
 
            # for every adjacent vertex `u` of `v`, reduce the in-degree of `u` by 1
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] - 1
 
            # include the current node in the path and mark it as discovered
            path.append(v)
            discovered[v] = True
 
            # recur
            findAllTopologicalOrderings(graph, path, discovered, n)
 
            # backtrack: reset in-degree information for the current node
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] + 1
 
            # backtrack: remove the current node from the path and
            # mark it as undiscovered
            path.pop()
            discovered[v] = False
 
    # print the topological order if all vertices are included in the path
    if len(path) == n:
        print(path)
 
 
# Print all topological orderings of a given DAG
def printAllTopologicalOrders(graph):
 
    # get the total number of nodes in the graph
    n = len(graph.adjList)
 
    # create an auxiliary space to keep track of whether the vertex is discovered
    discovered = [False] * n
 
    # list to store the topological order
    path = []
 
    # find all topological ordering and print them
    findAllTopologicalOrderings(graph, path, discovered, n)
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
 
    # total number of nodes in the graph (labelled from 0 to 7)
    n = 8
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # print all topological ordering of the graph
    printAllTopologicalOrders(graph)
 
