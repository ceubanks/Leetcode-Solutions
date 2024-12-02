'''
0-1 Knapsack Problem:
    - Given a set of items, each with a weight and a value, determine the items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
    - Each item can either be taken or not taken (0-1).

    Example:
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    Output: 7
'''

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If weight of current item is less than or equal to current capacity
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Time: O(n * capacity)
# Space: O(n * capacity)
print(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))

''' How is this optimized?
    - We are iterating from the back of the capacity to the front.
    - This way, we are using the previous computed values to compute the current values.
    - This is a form of dynamic programming known as "space optimized" version.
'''
def knapsack_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    
    return dp[capacity]

# Time Complexity: O(n * capacity)
# Space Complexity: O(capacity)
print(knapsack_optimized([2, 3, 4, 5], [3, 4, 5, 6], 5))