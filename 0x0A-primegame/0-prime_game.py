#!/usr/bin/python3
"""
Prime Game
"""


def generate_prime_numbers(n):
    """
    Generating prime numbers up to n using
    the Sieve of Eratosthenes algorithm.
    """
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers

    for current_prime in range(2, int(n**0.5) + 1):
        if sieve[current_prime]:
            for multiple in range(current_prime**2, n + 1, current_prime):
                sieve[multiple] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]


def isWinner(x, nums):
    """Determine the winner of x rounds of the prime game."""
    maria_wins = 0

    for n in nums:
        primes = generate_prime_numbers(n)
        remaining_primes = len(primes)

        if remaining_primes % 2 != 0:
            maria_wins += 1

    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None
