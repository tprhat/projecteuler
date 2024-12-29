def fib(max_value: int) -> int:
    # init cache
    cache: dict = {}
    cache[0] = 1
    cache[1] = 1
    cache[2] = 2

    i: int = 3
    total: int = 2
    while True:
        cache[i] = cache[i - 1] + cache[i - 2]
        if cache[i] > max_value:
            break
        if cache[i] % 2 == 0:
            total += cache[i]
        i += 1
    return total


if __name__ == "__main__":
    print(fib(4_000_000))
