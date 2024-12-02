
target_sum = 1000
count = 0
def dfs(node, cumulative_sum, prefix_sums):
    if not node:
        return
    
    cumulative_sum += node.val
    
    if cumulative_sum - target_sum in prefix_sums:
        count += prefix_sums[cumulative_sum - target_sum]

    prefix_sums[cumulative_sum] += 1

    dfs(node.left, cumulative_sum, prefix_sums)
    dfs(node.right, cumulative_sum, prefix_sums)

    prefix_sums[cumulative_sum] -= 1
    
    