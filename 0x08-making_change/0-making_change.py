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

    coins.sort(reverse=True)
    coins_needed = 0

    for coin in coins:
        coins_needed += total // coin
        total %= coin

    if total != 0:
        return -1
    else:
        return coins_needed
