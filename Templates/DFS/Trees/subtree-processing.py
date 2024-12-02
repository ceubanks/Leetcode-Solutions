'''
Description: Focus on processing or evaluating subtrees rooted at each node, often combining results from child subtrees to compute a result for the current node.
Characteristics:
	•	Post-order traversal is commonly used.
	•	Combine results from left and right children.
	•	Used to compute properties like height, diameter, or balance.
Common Problems:
	•	Balanced Binary Tree (Leetcode 110)
	•	Maximum Depth of Binary Tree (Leetcode 104)
	•	Diameter of Binary Tree (Leetcode 543)
'''
def dfs(node):
    if not node:
        return

    # Recursively process the left and right subtrees
    left_subtree = dfs(node.left)
    right_subtree = dfs(node.right)

    # Combine results to compute the current node's value
    current_result = process(left_subtree, right_subtree, node)

    return current_result


def process(left_subtree, right_subtree, node):
    # Process the left and right subtrees
    pass

# Time: O(n)
# Space: O(n)