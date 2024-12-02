from Trees import TreeNode
from typing import List

class Solution:
    def inorderTraversal(self, root:TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        
        def _inorder(node: TreeNode):
            if not node:
                return
            
            _inorder(node.left)
            res.append(node.val)
            _inorder(node.right)

        _inorder(root)
        return res
    
    #Time: O(n)
    #Space: O(n)