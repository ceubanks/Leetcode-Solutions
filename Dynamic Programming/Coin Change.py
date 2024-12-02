
# Time: O(n * amount)
# Space: O(amount)
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 2, 5], 11))

def coin_change_recursive(coins, amount, memo={}):
    # Base cases
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if memo[amount-1] != float('inf'):
        return memo[amount-1]
    
    # Recursive case
    min_coins = float('inf')
    # try every coin
    for coin in coins:
        # recursive call to see if we can make change for amount - coin
        res = coin_change_recursive(coins, amount - coin, memo)
        # if we can make change, update min_coins
        if res != -1:
            min_coins = min(min_coins, res + 1)
    
    # update memo with the minimum number of coins needed to make change for amount
    memo[amount-1] = min_coins if min_coins != float('inf') else -1
    
    return memo[amount-1]