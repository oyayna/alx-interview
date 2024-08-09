#!/usr/bin/env python3
"""0. Prime Game - Maria and Ben are playing a game"""

def is_winner(rounds, numbers):
    if rounds <= 0 or not numbers or rounds != len(numbers):
        return None

    ben_score, maria_score = 0, 0
    max_num = max(numbers)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_num + 1, i):
                primes[multiple] = False

    for num in numbers:
        prime_count = sum(primes[:num + 1])
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    return None

