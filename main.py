from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    frontier = []
    heappush(frontier, (0, 0, source))
    visited = dict()
    
    def helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            # adjacent one closest to heap
            distance, edges, node = heappop(frontier)
            if node in visited:
                return helper(visited, frontier)
            else:
                visited[node] = (distance, edges)
                for neighbor, weight in graph[node]:
                    heappush(frontier, (distance+weight, edges+1, neighbor))
                return helper(visited,frontier)
    
    return helper(visited,frontier)
    
  
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = dict() 
    frontier = deque()
    frontier.append(source)
    visited = set()
    def bfs_serial_helper(visited, frontier, parents):
        if len(frontier) == 0:
            return parents
        else:
            node = frontier.popleft()
            visited.add(node)
            for n in graph[node]:
              if n not in visited and n not in frontier:
                parents[n] = node 
                frontier.append(n)
            return bfs_serial_helper(visited, frontier, parents)
            
    return bfs_serial_helper(visited, frontier, parents)



def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    if destination in parents:
        return get_path(parents, parents[destination]) + parents[destination]
    else:
        return ''
