from collections import deque
from trees import TreeNode
from typing import List

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        averages = []

        while queue:
            n = len(queue)
            summ = 0

            for _ in range(n):
                node = queue.popleft()
                summ += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averages.append(summ / n)

        return averages
    
    # Time: O(n)
    # Space: O(n)