def find_largest_palindrome() -> int:
    largest = (0, 0, 0)
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            prod = i * j
            if check_palindrome(prod):
                # we can't just return the first palindrome we encounter since
                # there might be a bigger one that is hidden in the outer loop
                if prod > largest[0]:
                    largest = (prod, i, j)
    return largest


def check_palindrome(prod: int) -> bool:
    tmp = prod
    rev = 0
    while tmp > 0:
        dig = tmp % 10
        rev = rev * 10 + dig
        tmp //= 10
    # if num reversed == num we found a palindrome
    return prod == rev


if __name__ == "__main__":
    print(find_largest_palindrome())
