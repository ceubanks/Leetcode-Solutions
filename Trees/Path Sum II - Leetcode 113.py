from Trees import TreeNode
from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        
        def dfs(node: Optional[TreeNode], path: List[int], remainingSum: int):
            if not node:
                return
            
            path.append(node.val)
            remainingSum -= node.val
            
            if not node.left and not node.right and remainingSum == 0:
                res.append(path[:])

            dfs(node.left, path, remainingSum)
            dfs(node.right, path, remainingSum)

            path.pop()

        dfs(root, [], targetSum)
        return res
    
    #Time: O(n)
    #Space: O(n)