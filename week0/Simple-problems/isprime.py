from sumofdiv import sum_of_divisors


def is_prime(n):
    if sum_of_divisors(n) == (n + 1):
        return True
    else:
        return False


def main():
    print (is_prime(8))

if __name__ == '__main__':
    main()
