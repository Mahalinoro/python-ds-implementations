# Class Vertex
class Vertex:
    def __init__(self, key, value, n):
        self.id = key # Key for the index starting from 0
        self.value = value # value of the vertex
        self.connectedTo = [0] * n 
    
    # Method that returns the vertex
    def __str__(self): 
        return str(self.value) + " -> " + str(self.connectedTo)

    # Method to add an adjacent vector to the vertex
    # Time complexity => O(1)
    # Space complexity => O(1)
    def addNeighbor(self, n, weight):
        if n != 0:
            self.connectedTo[n-1] = weight
        else:
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

# Class UndirectedWeightedGraph => Cannot be used for directed graph
class UndirectedWeightedGraph:
    def __init__(self, isUndirected=True):
        self.graph = []
        self.isUndirected = isUndirected
        self.totalVertices = 0
    

    # Method that prints the graph in the form an adjancency matrix
    # Time complexity => O(V)
    # Space complexity => O(1)
    def printGraph(self):
        for vertex in range(len(self.graph)):
            print(self.graph[vertex])

    # Method that prints it as a simple representation of a list of lists
    # Time complexity => O(V)
    # Space complexity => O(V+E)
    def printTest(self):
        fullGraph = []
        for vertex in self.graph:
            fullGraph.append(vertex.connectedTo)
        return fullGraph

    # Method that inserts a vertex in the graph and update the other vertex having the same index in the graph
    # Time Complexity => O(V)
    # Space Complexity => O(1)
    def insertVertex(self, v):
        if self.graph == []:
            self.totalVertices += 1
            newVertex = Vertex(0,v,self.totalVertices)
            self.graph.append(newVertex)

        else:
            if v not in [vertex.id for vertex in self.graph]:
                newVertex = Vertex(self.totalVertices,v, self.totalVertices)
                self.graph.append(newVertex)
                self.totalVertices += 1
                self.updateRow()
    
    # Method that update the rows with 0 while there is a new vertex inserted
    # Time Complexity => O(V)
    # Space Complexity => O(1)
    def updateRow(self):
        for vertex in self.graph:
            vertex.connectedTo.append(0)

    # Method that inserts an edge between two vertices
    # Time Complexity => O(V)
    # Space Complexity => O(1)
    def insertEdge(self, v1, v2, weight):
        if v1 not in [vertex.value for vertex in self.graph]:
            self.insertVertex(v1)
        if v2 not in [vertex.value for vertex in self.graph]:
            self.insertVertex(v2)
        
        for vertex in self.graph:
            if vertex.value == v1:
                vertex.addNeighbor(v2, weight)
            if vertex.value == v2:
                vertex.addNeighbor(v1, weight)

    # Method that delete a vertex from the graph
    # Time Complexity => O(V)
    # Space Complexity => O(1)
    def deleteVertex(self, v):
        for vertex in self.graph:
            if v == vertex.value:
                self.graph.pop(vertex.id)
                self.totalVertices -= 1

        for vertex in self.graph:
            vertex.connectedTo.pop(v-1)

    # Method that delete the edge between to vertices
    # Time Complexity => O(V)
    # Spae Complexity => O(1)
    def deleteEdge(self, v1, v2):
        for vertex in self.graph:
            if v1 == vertex.value:
                vertex.connectedTo[v2-1] = 0
            if v2 == vertex.value:
                vertex.connectedTo[v1-1] = 0

    # Method that updated the weight between the vertex source and a vertex adjacent to it
    # Time Complexity => O(V)
    # Space Complexity => O(1)
    def updateWeight(self, v1, v2, value):
        for vertex in self.graph:
            if v1 == vertex.value:
                vertex.connectedTo[v2-1] = value
            if v2 == vertex.value:
                vertex.connectedTo[v1-1] = value