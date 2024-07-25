
from typing import Optional
from trees import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_path_sum(root: Optional[TreeNode], curr_sum: int) -> bool:
            if not root:
                return False
            
            curr_sum += root.val

            if not root.left and not root.right and curr_sum == targetSum:
                return True
            
            return has_path_sum(root.left, curr_sum) or has_path_sum(root.right, curr_sum)
        
        return has_path_sum(root, 0)