'''
Given an undirected graph, determine if it is bipartite.

A bipartite graph is a graph whose vertices can be divided into two disjoint (independent) sets
such that every edge connects a vertex in one set to a vertex in the other set.

This algorithm determines if a graph is bipartite by attempting to color its nodes using two colors. It does so using a Breadth-First Search (BFS):
	1.	Start with an uncolored node and color it with one color.
	2.	Use BFS to visit each of its neighbors, coloring them with the opposite color.
	3.	Continue the BFS, assigning colors to each newly reached node in the same alternating manner.

If at any point you find that an edge connects two nodes of the same color, the graph is not bipartite. This situation arises if and only if the graph contains an odd-length cycle. Why? Because if you try to alternate colors along a cycle of odd length, when you return to the starting point, you’ll be forced to assign a different color than what you started with, creating a contradiction.

BFS is particularly useful here because it explores nodes layer by layer, based on their distance from the starting point. Nodes at the same BFS level should all be colored differently from nodes in the levels above or below. If you find a conflict—an edge connecting two nodes on the same level—that indicates an odd-length cycle. Thus, BFS neatly exposes whether proper two-coloring is possible, letting you determine if the graph is bipartite.

'''

from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj = {i: [] for i in range(len(graph))}
        for i in range(len(graph)):
            for j in graph[i]:
                adj[i].append(j)
                adj[j].append(i)

        color = [-1] * len(graph)

        is_bipartite = True

        # Traverse the graph and color the nodes
        for i in range(len(graph)):

            # If the node is uncolored, assign first color
            if color[i] == -1:
                color[i] = 0

                # use bfs to color the node
                is_bipartite = self._bfs(i, color, adj)
                if not is_bipartite:
                    return False
        return True
    
    def _bfs(self, node, color, adj):
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    