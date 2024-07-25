
from typing import Optional
from trees import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        count = [0]
        kth_smallest = [0]

        def _inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
        
            _inorder(node.left)
            count[0] += 1

            if count[0] == k:
                kth_smallest[0] = node.val
                return
            
            _inorder(node.right)

        _inorder(root)
        return kth_smallest[0]
        

# Time: O(k)
# Space: O(1)