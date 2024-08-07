#!/usr/bin/python3
# Prime game winner determination


def isWinner(x, nums):
    """Determine who won the most rounds."""

    def sieve(n):
        """Generate list of primes up to n using Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def game_winner(n):
        """Determine the winner of the game with n."""
        primes = sieve(n)
        remaining = set(range(1, n + 1))
        turn = 0  # Maria starts (0), Ben is (1)

        while primes:
            p = primes.pop(0)
            if p > n:
                break
            if p in remaining:
                # Remove multiples of p
                for multiple in range(p, n + 1, p):
                    remaining.discard(multiple)
                turn = 1 - turn  # Switch turn

        return "Maria" if turn == 1 else "Ben"

    if x == 0:
        return None

    win_count = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = game_winner(n)
        if winner:
            win_count[winner] += 1

    if win_count["Maria"] > win_count["Ben"]:
        return "Maria"
    elif win_count["Ben"] > win_count["Maria"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
