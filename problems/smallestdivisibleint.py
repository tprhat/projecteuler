from math import floor, log, sqrt


# create a primes map
primes = [2, 3, 5, 7, 11, 13, 17, 19]


def find_smallest():
    k = 20
    N = 1
    check = True
    limit = sqrt(k)
    for prime in primes:
        a = 1
        if check:
            if prime <= limit:
                a = floor(log(k) / log(prime))
            else:
                check = False
        print(prime, a)
        N *= prime**a
    return N


if __name__ == "__main__":
    print(find_smallest())
