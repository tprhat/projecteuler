import math


def sum_primes(n: int) -> int:
    primes = [2, 3, 5]
    i = 7
    while i < n:
        if is_prime(i, primes):
            primes.append(i)
        i += 2
    return sum(primes)


def is_prime(x: int, primes: list) -> bool:
    for p in primes:
        if x % p == 0:
            return False
        # we can check only the primes that are
        # smaller than sqrt(x)
        if p > math.sqrt(x):
            break
    return True


if __name__ == "__main__":
    print(sum_primes(2_000_000))
