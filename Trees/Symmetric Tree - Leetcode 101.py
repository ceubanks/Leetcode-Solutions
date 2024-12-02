from Trees import TreeNode
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and _dfs(left.left, right.right) and _dfs(left.right, right.left)
        
        return _dfs(root.left, root.right)
    
    #Time: O(n)
    #Space: O(n)