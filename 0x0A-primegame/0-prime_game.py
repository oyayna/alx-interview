#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""

def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    primes = [1 for _ in range(sorted(nums)[-1] + 1)]
    primes[0], primes[1] = 0, 0
    for i in range(2, len(primes)):
        rm_multiples(primes, i)

    for num in nums:
        if sum(primes[:num + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None

def rm_multiples(ls, x):
    """Removes multiples of primes"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break

