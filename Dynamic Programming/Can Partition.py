
def can_partition(nums):
    """
    Determines if the array can be partitioned into two subsets with equal sum.

    Args:
        nums (List[int]): A list of positive integers.

    Returns:
        bool: True if the array can be partitioned into two subsets with equal sum, False otherwise.
    """

    total_sum = sum(nums)
    # If the total sum is odd, partitioning into two equal subsets is impossible.
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    dp = [False] * (target_sum + 1)
    dp[0] = True # Base case: zero sum is always achievable.

    for num in nums:
        for i in range(target_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target_sum]

print(can_partition([1, 5, 11, 5]))