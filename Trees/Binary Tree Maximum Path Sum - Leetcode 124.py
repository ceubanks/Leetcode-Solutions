from Trees import TreeNode
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        
        def dfs(root):
            if not root:
                return 0
            # post order traversal
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            # if the max path sum is negative, we don't want to consider it
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # update the max path sum with the current root value and the left and right max path sums
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return the max path sum with the current root value and the left or right max path sum
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
    