#!/usr/bin/python3
"""0. Change comes from within"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: The fewest number of coins needed to meet total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins you have, return -1.
    """

    if total <= 0:
        return 0

    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                min_coins[amount] = (min(min_coins[amount],
                                     min_coins[amount - coin] + 1))

    if min_coins[total] == total + 1:
        return -1
    else:
        return min_coins[total]
