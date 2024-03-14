#!/usr/bin/python3
"""The module defines the isWinner function
"""


def isWinner(x, nums):
    """The isWinner funtion
    x - number of games to play
    nums - list of numbers
    """
    def is_prime(num):
        """The function determines if num is a prime number
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def calculate_winner(n):
        """calculate_winner function for players
        """
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        total_primes = set(primes)
        maria_wins = True

        while total_primes:
            current_player = maria_wins
            for prime in primes:
                if prime in total_primes:
                    current_player = not current_player
                    multiples = set(range(prime, n + 1, prime))
                    total_primes -= multiples

            maria_wins = not maria_wins

        return "Maria" if maria_wins else "Ben"

    winners = [calculate_winner(n) for n in nums]
    maria_wins_count = winners.count("Maria")
    ben_wins_count = winners.count("Ben")

    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None
