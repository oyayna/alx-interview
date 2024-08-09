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

    ben_score = 0
    maria_score = 0

    primes = [1 for _ in range(max(nums) + 1)]
    primes[0], primes[1] = 0, 0
    for i in range(2, len(primes)):
        remove_multiples(primes, i)

    for num in nums:
        if sum(primes[:num + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None

def remove_multiples(primes, x):
    """Removes multiples of primes"""
    for i in range(2, len(primes)):
        try:
            primes[i * x] = 0
        except (ValueError, IndexError):
            break

