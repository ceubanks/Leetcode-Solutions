from typing import Optional
from Trees import TreeNode

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first, self.second, self.prev = None, None, None
        def _inorder(node: Optional[TreeNode], prev: Optional[TreeNode], first: Optional[TreeNode], second: Optional[TreeNode]):
            if not node:
                return
            
            _inorder(node.left, prev, first, second)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            _inorder(node.right, self.prev, self.first, self.second)

        _inorder(root, None, None, None)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    #Time: O(n)
    #Space: O(n)