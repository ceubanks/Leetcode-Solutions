from Trees import TreeNode
from typing import Optional

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return 1 + self.minDepth(root.right) #only go right
        
        if not root.right:
            return 1 + self.minDepth(root.left) #only go left
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        