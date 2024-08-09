#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game."""

def isWinner(x, nums):
    """Determine the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of numbers.

    Returns:
        str: The winner ("Ben" or "Maria"), or None if no winner.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben, maria = 0, 0

    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0

    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    return None

def rm_multiples(ls, x):
    """Removes multiples of primes."""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break

