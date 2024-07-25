
from typing import Optional
from trees import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _dfs(node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            if not node:
                return True
            
            if min_val < node.val < max_val:
                return _dfs(node.left, min_val, node.val) and _dfs(node.right, node.val, max_val)
            
            return False
        
        return _dfs(root, float('-inf'), float('inf'))