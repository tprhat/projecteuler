def find_largest_prime(num: int) -> int:
    factor: int = 2
    factors = set()
    while True:
        if num % factor == 0:
            num /= factor
            factors.add(factor)
        else:
            factor += 1
        if num == 1:
            break
    return max(factors)


if __name__ == "__main__":
    print(find_largest_prime(600_851_475_143))
