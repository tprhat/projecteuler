def find_special_triplet(n: int) -> int:
    for a in range(3, (n - 3) // 3):
        for b in range(a + 1, (n - 1 - a) // 2):
            c = n - a - b
            if a**2 + b**2 == c**2:
                print(a, b, c)
                return a * b * c
    return -1


if __name__ == "__main__":
    print(find_special_triplet(1000))
