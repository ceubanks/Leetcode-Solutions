
from typing import Optional
from trees import TreeNode

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        min_difference = [float('inf')]
        prev = [None]

        def _inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            _inorder(node.left)
            
            if prev[0] is not None:
                min_difference[0] = min(min_difference, abs(node.val - prev[0].val))

            prev[0] = node.val

            _inorder(node.right)

        _inorder(root)
        return min_difference[0]