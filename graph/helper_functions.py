import collections

# function FindPath(v1,v2) that inputs two vertices in a directed weighted graph
# And finds a path from v1 to v2 outputting an array of edges starting from v1 and ending at v2 
# Such that there is a directed edge from v1 to the next and so on until v2. 
# Return False if no path exists.

# Time complexity => O(V*E)
# Space complexity => O(E)
def FindPath(graph, root, d): 
    visited, queue = set(), collections.deque([root]) # Using queue 
    visited.add(root) # Visited to store the vertex that has been visited
    path = [] # Path to store the edges 

    # If queue is not empty
    while queue: 
        # Remove the vertex in the queue
        vertex = queue.popleft()
        # if the current vertex == to final destination, then return the path
        if vertex == d:
            return path
        
        # Looping through the vertices adjacent to the current vertex
        for neighbour in graph.graph[vertex].connectedTo: 
            # if the vertex is not in visited 
            # Then add it to the visited set
            # And append it to the queue
            # Also, append the edges to the path
            if neighbour.id not in visited:
                visited.add(neighbour.id) 
                queue.append(neighbour.id)
                path.append([graph.graph[vertex].id, neighbour.id])  
                # if vertex == destination then stop the loop
                if neighbour.id == d:       
                    break      

    return False


# function FindShortestLength2(UWG) that inputs an Undirected Weighted Graph 
# And finds the shortest (in terms of sums of weight) path of length 2 outputting the 3 vertices that form the path of length 2. 
# Edges may not be repeated in the path.
import queue

# Time Complexity => O(V^2)
# Space Complexity => O(V)
def FindShortestLength2(UWG):
    shortestPath2 = []
    minSumWeight = 99999

    for vertex in UWG.graph:
        path = bfs(UWG, vertex)
        total = calculateSumWeight(path)
        if total < minSumWeight:
            minSumWeight = total
            shortestPath2 = [path[i][0] for i in range(len(path))]             

    return shortestPath2

# Implementing a customized bfs 
# Still needs to be optimized
def bfs(graph, start):
    frontier = queue.Queue()
    frontier.put(start)
    explored = set()
    path = [[start, 0]]
    previous = 0

    while frontier:
        current_vertex = frontier.get()
        if current_vertex in explored:
            continue
        
        weight = [graph.graph[current_vertex].connectedTo[neighbor] for neighbor in graph.graph[current_vertex].connectedTo]
        minWeight = min(weight)

        for neighbor in graph.graph[current_vertex].connectedTo: 
            if graph.graph[current_vertex].connectedTo[neighbor] == minWeight:
                if neighbor.id not in explored: 
                    frontier.put(neighbor.id)
                    path.append([neighbor.id, graph.graph[current_vertex].connectedTo[neighbor]])    
                    if len(path) == 3:
                        return path
                else:
                    weight.remove(minWeight)
                    if weight == []:
                        path.pop(1)
                        weight = [graph.graph[previous].connectedTo[neighbor] for neighbor in graph.graph[previous].connectedTo]
                        weight.remove(min(weight))
                        minWeight = min(weight)
                        for neighbor in graph.graph[previous].connectedTo:
                            if graph.graph[previous].connectedTo[neighbor] == minWeight: 
                                if neighbor.id not in explored:
                                    frontier.put(neighbor.id)
                                    path.append([neighbor.id, graph.graph[previous].connectedTo[neighbor]])    
                                    if len(path) == 3:
                                        return path                  

                    else:
                        minWeight = min(weight)
                        i = iter(graph.graph[current_vertex].connectedTo)
                        for vertex in i:
                            if graph.graph[current_vertex].connectedTo[vertex] == minWeight:
                                frontier.put(vertex.id)
                                path.append([vertex.id,  graph.graph[current_vertex].connectedTo[vertex]])
                                if len(path) == 3:
                                    return path                

        explored.add(current_vertex)
        previous = current_vertex
    
# CalculateSumWeight function helper to calculate the weight of the path from bfs
# Time Complexity => O(V)
# Space Complexity => O(1)
def calculateSumWeight(path):
    sumWeight = 0
    for i in range(len(path)):
        sumWeight += path[i][1]
    return sumWeight



# Function FindFurthest(DWG, v, metric) where DWG is a directed-weighted-graph type, v is a vertex in the DWG, and metric is either:
#‘level’ - in which you should find a vertex in DWG that is reachable using directed edges from v but is the furthest away in terms of number of edges.
#‘weight’ - in which you should find a vertex in DWG that is reachable using directed edges from v but is the furthest away in terms of the sum of the weight of edges in the shortest path to it.
from question_one import DirectedWeightedGraph
import collections

def Dijkstras(graph, source, g_nodes) :    
    # Initialize the distance of all the nodes from source to infinity
    distance = [999999999999] * (g_nodes + 1)
    # Distance of source node to itself is 0
    distance[source] = 0

    # Create a dictionary of { node, distance_from_source }
    dict_node_length = {source: 0}

    while dict_node_length :

        # Get the key for the smallest value in the dictionary
        # i.e Get the node with the shortest distance from the source
        source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
        del dict_node_length[source_node]

        for node_dist in graph.graph[source_node].connectedTo :
            adjnode = node_dist.id
            length_to_adjnode = graph.graph[source_node].getWeight(node_dist)

            # Edge relaxation
            if distance[adjnode] > distance[source_node] + length_to_adjnode :
                distance[adjnode] = distance[source_node] + length_to_adjnode
                dict_node_length[adjnode] = distance[adjnode]

    return [i for i in range(len(distance[1:])) if distance[i] == max(distance[1:])][0]



def FindFurthest(DWG, v, metric):
    if metric == 'level':
        n_edges = 0
        visited, queue = set(), collections.deque([v]) # Using queue 
        visited.add(v) # Visited to store the vertex that has been visited
        vertices = []

        # If queue is not empty
        while queue: 
            # Remove the vertex in the queue
            vertex = queue.popleft()
            vertices.append(vertex)

            # Looping through the vertices adjacent to the current vertex
            for neighbour in DWG.graph[vertex].connectedTo: 
                # if the vertex is not in visited 
                # Then add it to the visited set
                # And append it to the queue
                # Also, append the edges to the path
                if neighbour.id not in visited:
                    queue.append(neighbour.id)                
                    visited.add(neighbour.id) 

                # path.append([vertex, neighbour.id])
        return vertices[-1]
        
    elif metric == 'weight':
       max_v = Dijkstras(DWG, v, len(DWG.graph))
       return max_v
        # Find all the path starting from v with highest weight
