from typing import Optional
from trees import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left_height = height(root.left)
            if balanced[0] == False:
                return 0
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            
            return max(left_height, right_height) + 1
        
        height(root)
        return balanced[0]
            
        