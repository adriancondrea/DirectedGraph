from directed_graph import DirectedGraph

'''1. Write a program that, given a directed graph and two vertices, finds a lowest length path between them, by using 
a forward breadth-first search from the starting vertex.'''

def findLowestLengthPathBFS(graph, start, end):
    '''
    find the lowest length path between start and end, in graph, using a forward BFS from the starting vertex
    if start or end are not valid vertices in the graph, we raise ValueError
    if there is no path between start and end, we raise ValueError
    :param graph: the given graph
    :param start: the starting vertex
    :param end: the ending vertex
    :return: returns the path from start to end if it exists, otherwise it raises ValueError
    '''
    #if the start or end are not valid, we raise ValueError
    if not graph.valid_vertex(start) or not graph.valid_vertex(end):
        raise ValueError("invalid start / end!")
    # we remember all the visited nodes
    visited = []
    # we remember all the possible paths in a queue
    queue = [[start]]
    if start == end:
        return [] # case when start = end, the path is empty
    while queue:    #while we have paths unchecked
        #we pop the first path from the queue
        path = queue.pop(0)
        #we get the last node in the path
        vertex = path[-1]
        # if the vertex is not visited, for each of its outbound vertex, we create a new path from the
        # previous one by adding the outbound vertex. If the outbound vertex coincides with the end vertex
        # we return the path we just created
        if vertex not in visited:
            outboundVertices = graph._outbound[vertex]
            for outbound in outboundVertices:
                newPath = list(path)
                newPath.append(outbound)
                queue.append(newPath)
                if outbound == end:
                    return newPath
            #we add the vertex to the list of visited vertices
            visited.append(vertex)
    #if we got there means we've visited all vertices that can be visited from start, and we couldn't find
    #a path between start and end, so we raise a ValueError
    raise ValueError("No path between start and end")



