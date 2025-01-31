def find_primes(n: int) -> int:
    primes = [2, 3, 5]
    i = 7
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)
        i += 2
    return primes[-1]


def is_prime(x: int, primes: list) -> bool:
    for p in primes:
        if x % p == 0:
            return False
    return True


if __name__ == "__main__":
    print(find_primes(10001))
