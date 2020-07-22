# Class Vertex
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # The vertices that are adjacent to the initial vertex

    # Method returning the vertex
    def __str__(self):
        return str(self.id) + " -> " + str({(neighbor.id, self.connectedTo[neighbor]) for neighbor in self.connectedTo}) 
    
    # Method to add an adjacent vector to the vertex
    # Time complexity => O(1)
    # Space complexity => O(1)
    def addNeighbor(self, n, weight=0): # n = neighbor
        self.connectedTo[n] = weight
    
    # Method returning the key/id of the vertex
    # Time complexity => O(1)
    # Space complexity => O(1)
    def getId(self):
        return self.id
    
    # Method returning the weight of the vertex from a vertex adjacent to it
    # Time complexity => O(1)
    # Space complexity => O(1)
    def getWeight(self, n):
        return self.connectedTo[n]

# Class DirectedWeightedGraph / can be used as undirected 
class DirectedWeightedGraph:
    def __init__(self, isUndirected=False):
        self.graph = {} # Initialized as a dictionary
        self.totalVertices = 0
        self.isUndirected = isUndirected # True if undirected

    # Method that prints the graph in the form an adjancency list
    # Time complexity => O(V)
    # Space complexity => O(1)
    def printGraph(self):
        for k in self.graph:
            print(self.graph[k])
    
    # Method that prints it as a simple representation of a dictionary
    # Time complexity => O(V^2)
    # Space complexity => O(V+E)
    def printTest(self):
        fullGraph = {}
        for key in self.graph:
            fullGraph[key] = [vertex.id for vertex in self.graph[key].connectedTo]
        return fullGraph

    # Method that inserts a vertex in the graph
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def insertVertex(self, v):
        if v not in self.graph:
            newVertex = Vertex(v)
            self.graph[v] = newVertex
            self.totalVertices += 1

    # Method that inserts an edge between two vertices
    # Time Complexity => O(1)
    # Space Complexity => O(1)
    def insertEdge(self, v1, v2, weight=0):
        if v1 not in self.graph:
            newVertex = self.insertVertex(v1)
        if v2 not in self.graph:
            newVertex = self.insertVertex(v2)
        
        self.graph[v1].addNeighbor(self.graph[v2], weight)

    # Method that delete a vertex from the graph
    # Time Complexity => O(V*E)
    # Space Complexity => O(1)
    def deleteVertex(self, v):
        if v in self.graph:
            self.graph.pop(v)
            self.totalVertices -= 1

        for key in self.graph:
            for k in self.graph[key].connectedTo:
                if v == k.id:
                    return self.graph[key].connectedTo.pop(k)

    # Method that delete the edge between to vertices
    # Time Complexity => O(V)
    # Spae Complexity => O(1)
    def deleteEdge(self, v1, v2):
        if v1 and v2 in self.graph:
            for k in self.graph[v1].connectedTo:
                if v2 == k.id:
                    return self.graph[v1].connectedTo.pop(k)

    # Method that updated the weight between the vertex source and a vertex adjacent to it
    # Time Complexity => O(V)
    # Space Complexity => O(1)
    def updateWeight(self, v1, v2, value):
        if v1 and v2 in self.graph:
            for k in self.graph[v1].connectedTo:
                if v2 == k.id:
                    return self.graph[v1].connectedTo.update({k:value})
            