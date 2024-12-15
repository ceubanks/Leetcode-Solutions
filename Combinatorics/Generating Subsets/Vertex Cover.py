'''
Vertex Cover: Given a graph, find the minimum (smallest) subset of vertices to touch each edge.

This is a NP-hard problem, so we will use a backtracking approach to find a solution.

The algorithm uses a depth-first search (DFS) to explore the graph and find a vertex cover 
(a set of vertices that touches every edge in the graph). The algorithm starts by 
iterating over each node in the graph and calling the DFS function from that node.

The DFS function marks the current node as visited and recursively visits all its 
unvisited neighbors. If a neighbor is not visited, the DFS function is called from 
that neighbor. The algorithm ensures that all edges are covered by adding both the 
current node and its neighbor to the cover set.

Finally, the algorithm returns the cover set, which contains the minimum number of 
vertices that touch every edge in the graph.

How do we know if this is the smallest subset? Because we are using a backtracking 
approach, we are exploring all possible subsets of vertices. The first subset we
find is the smallest subset.

This is a good solution, but it is not the most efficient solution. There are 
other algorithms that are more efficient, but this is a good starting point.
'''

# Find the smallest subset of vertices to touch each edge.
def vertex_cover(graph):
    def _dfs(node, visited, cover):
        # Base case: If the node is already visited, return
        if node in visited:
            return
        
        # Mark the node as visited
        visited.add(node)

        # Recursively visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                _dfs(neighbor, visited, cover)
                cover.add(node)
                cover.add(neighbor)
    
    # Initialize visited and cover sets
    visited = set()
    cover = set()
    
    # Start the DFS from each node in the graph
    for node in graph:
        if node not in visited:
            _dfs(node, visited, cover)
    
    # Return the cover set
    return cover

def efficient_vertex_cover(graph):
    # This is a more efficient algorithm that uses a greedy approach to find a vertex cover.
    # It is not guaranteed to find the smallest subset, but it is faster than the backtracking approach.
    cover = set()
    for edge in graph:
        if edge not in cover:
            cover.add(edge[0])
            cover.add(edge[1])
    return cover


def binary_ordering_subsets(n):
    """
    Generate all subsets of a set with elements 0 to n-1 in binary ordering.

    Args:
    n (int): The number of elements in the set.

    Returns:
    List[List[int]]: A list of subsets, where each subset is represented as a list of integers.
    """
    subsets = []
    # Iterate over all possible subsets (2^n subsets)
    for i in range(1 << n):
        subset = []
        # Check each bit position to determine if the element should be included in the subset
        for j in range(n):
            if i & (1 << j):
                subset.append(j)
        subsets.append(subset)

    return subsets


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    print(vertex_cover(graph))

if __name__ == "__main__":
    main()