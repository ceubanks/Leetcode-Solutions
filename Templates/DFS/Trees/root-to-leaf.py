
'''
Description: These problems involve traversing from the root of the tree to its leaves, often collecting or computing information along the path.
Characteristics:
	•	Accumulate data (like paths, sums) during traversal.
	•	Process or record data when a leaf node is reached.
	•	Often require passing state information through recursive calls.
Common Problems:
	•	Binary Tree Paths (Leetcode 257)
	•	Sum Root to Leaf Numbers (Leetcode 129)
	•	Path Sum II (Leetcode 113)
'''

def traverse(node, state):
    if not node:
        return
    
    # Update the state with the current node's value
    state.append(node.val)

    # If the current node is a leaf node, process the state
    if not node.left and not node.right:
        print(state)

    # Recursively traverse the left and right subtrees
    traverse(node.left, state)
    traverse(node.right, state)

    # Remove the current node's value from the state
    state.pop()