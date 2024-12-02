Coding Interview Patterns Cheatsheet
Table of Contents
	1.	Sliding Window
	2.	Two Pointers
	3.	Fast and Slow Pointers
	4.	Merge Intervals
	5.	Cyclic Sort
	6.	In-place Reversal of a Linked List
	7.	Tree Traversals
	8.	Binary Search
	9.	Backtracking
	10.	Breadth-First Search (BFS)
	11.	Depth-First Search (DFS)
	12.	Topological Sort
	13.	K-way Merge
	14.	Subsets
	15.	Dynamic Programming
	16.	Heap (Priority Queue)
	17.	Trie (Prefix Tree)
	18.	Union Find (Disjoint Set)
	19.	Greedy Algorithms
	20.	Graph Algorithms
	21.	Matrix Traversal
	22.	Bit Manipulation
	23.	Segment Trees
	24.	Fenwick Trees (Binary Indexed Trees)
	25.	Knuth-Morris-Pratt (KMP) Algorithm
Sliding Window
Description
Used to solve problems involving subarrays or substrings of a contiguous nature. Efficient for fixed-size or variable-size window problems.
Template
def sliding_window(arr):
    window_start = 0
    max_length = 0
    for window_end in range(len(arr)):
        # Expand the window by including arr[window_end]
        # If window size exceeds constraint, shrink from the start
        while condition_not_satisfied:
            # Remove arr[window_start] from window
            window_start += 1
        # Update the result if necessary
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
Back to Top
Two Pointers
Description
Involves two pointers moving through the data structure, often from both ends towards the center or at different speeds.
Template
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Perform logic with arr[left] and arr[right]
        if condition:
            left += 1
        else:
            right -= 1
Back to Top
Fast and Slow Pointers
Description
Used to detect cycles in linked lists or arrays by moving pointers at different speeds.
Template
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # Move one step
        fast = fast.next.next     # Move two steps
        if slow == fast:
            return True
    return False
Back to Top
Merge Intervals
Description
Merges overlapping intervals and is useful in scheduling and calendar applications.
Template
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x.start)
    merged = []
    for interval in intervals:
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        else:
            merged[-1].end = max(merged[-1].end, interval.end)
    return merged
Back to Top
Cyclic Sort
Description
Efficiently sorts an array containing numbers in a known range with O(n) time and O(1) space.
Template
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    return nums
Back to Top
In-place Reversal of a Linked List
Description
Reverses a linked list in place without extra memory.
Template
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev
Back to Top
Tree Traversals
Pre-order Traversal
def preorder(root):
    if root:
        # Process root
        preorder(root.left)
        preorder(root.right)
In-order Traversal
def inorder(root):
    if root:
        inorder(root.left)
        # Process root
        inorder(root.right)
Post-order Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        # Process root
Level-order Traversal (BFS)
from collections import deque
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # Process node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
Back to Top
Binary Search
Description
Searches for a target value in a sorted array with O(log n) time complexity.
Template
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found
Back to Top
Backtracking
Description
Explores all potential solutions by building them incrementally.
Template
def backtrack(path, options):
    if end_condition:
        result.append(path.copy())
        return
    for option in options:
        # Choose
        path.append(option)
        # Explore
        backtrack(path, updated_options)
        # Un-choose
        path.pop()
Back to Top
Breadth-First Search (BFS)
Description
Traverses a graph level by level, useful for finding the shortest path.
Template
from collections import deque
def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        # Process node
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
Back to Top
Depth-First Search (DFS)
Recursive Template
def dfs(node, visited=set()):
    if node in visited:
        return
    visited.add(node)
    # Process node
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
Iterative Template
def dfs_iterative(start_node):
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        # Process node
        for neighbor in node.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
Back to Top
Topological Sort
Description
Orders nodes in a directed acyclic graph (DAG) based on dependencies.
Template
def topological_sort(graph):
    visited = set()
    stack = []
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        stack.append(node)
    for node in graph:
        dfs(node)
    return stack[::-1]
Back to Top
K-way Merge
Description
Merges k sorted arrays or lists into a single sorted array.
Template
import heapq
def merge_k_lists(lists):
    min_heap = []
    for idx, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], idx, 0))
    result = []
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    return result
Back to Top
Subsets
Description
Generates all possible subsets (the power set) of a set.
Template
def subsets(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result
Back to Top
Dynamic Programming
Memoization (Top-Down)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
Tabulation (Bottom-Up)
def fib(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]
Back to Top
Heap (Priority Queue)
Description
Used to efficiently retrieve the minimum or maximum element.
Min-Heap Template
import heapq
def min_heap_operations(nums):
    heapq.heapify(nums)  # Transform list into a heap
    heapq.heappush(nums, item)  # Add item to heap
    smallest = heapq.heappop(nums)  # Pop smallest item
Back to Top
Trie (Prefix Tree)
Description
A tree-like data structure used for efficient retrieval of keys, often strings.
Template
class TrieNode:
    def init(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def init(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True
    def search(self, word):
        node = self._find_node(word)
        return node.is_end_of_word if node else False
    def starts_with(self, prefix):
        return self._find_node(prefix) is not None
    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return None
        return node
Back to Top
Union Find (Disjoint Set)
Description
Data structure to track a set of elements partitioned into disjoint subsets.
Template
class UnionFind:
    def init(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
Back to Top
Greedy Algorithms
Description
Makes the locally optimal choice at each stage with the hope of finding a global optimum.
Template
def greedy_algorithm(items):
    # Sort items based on some criterion
    items.sort(key=lambda x: x.value, reverse=True)
    result = []
    for item in items:
        if acceptable(item):
            result.append(item)
    return result
Back to Top
Graph Algorithms
Dijkstra’s Algorithm (Shortest Path)
import heapq
def dijkstra(graph, start):
    min_heap = [(0, start)]
    distances = {start: 0}
    while min_heap:
        current_distance, node = heapq.heappop(min_heap)
        for neighbor, weight in graph[node]:
            distance = current_distance + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    return distances
Bellman-Ford Algorithm
def bellman_ford(graph, start, num_vertices):
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    for _ in range(num_vertices - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    # Check for negative-weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    return distances
Back to Top
Matrix Traversal
Description
Techniques to traverse a matrix in various orders.
4-Directional Traversal
def traverse_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or visited[r][c]:
            return
        visited[r][c] = True
        # Process cell
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(r + dr, c + dc)
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                dfs(r, c)
Back to Top
Bit Manipulation
Description
Efficiently manipulates bits to solve problems.
Common Operations
	•	Check if the ith bit is set
def is_bit_set(num, i):
    return (num & (1 << i)) != 0
	•	Set the ith bit
def set_bit(num, i):
    return num | (1 << i)
	•	Clear the ith bit
def clear_bit(num, i):
    return num & ~(1 << i)
	•	Toggle the ith bit
def toggle_bit(num, i):
    return num ^ (1 << i)
Back to Top
Segment Trees
Description
A tree data structure for storing intervals or segments, allowing fast queries.
Template
class SegmentTreeNode:
    def init(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0  # Or any other aggregate function
        self.left = self.right = None
def build_segment_tree(nums, start, end):
    if start > end:
        return None
    node = SegmentTreeNode(start, end)
    if start == end:
        node.sum = nums[start]
    else:
        mid = (start + end) // 2
        node.left = build_segment_tree(nums, start, mid)
        node.right = build_segment_tree(nums, mid + 1, end)
        node.sum = node.left.sum + node.right.sum
    return node
Back to Top
Fenwick Trees (Binary Indexed Trees)
Description
A data structure that provides efficient methods for calculation and manipulation of the prefix sums.
Template
class FenwickTree:
    def init(self, size):
        self.sums = [0] * (size + 1)
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & -i
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & -i
        return res
Back to Top
Knuth-Morris-Pratt (KMP) Algorithm
Description
An efficient pattern-searching algorithm for strings.
Template
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0  # index for text[], index for pattern[]
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            print("Found pattern at index", i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
Back to Top
Note: Replace placeholder comments and variables with problem-specific logic when using these templates.
Feel free to save this cheatsheet as a file for your coding interview preparation. Good luck!