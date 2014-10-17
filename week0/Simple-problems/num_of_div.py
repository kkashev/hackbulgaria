from isprime import is_prime


def prime_number_of_divisors(n):
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return is_prime(count)


def main():

    print (prime_number_of_divisors(9))


if __name__ == '__main__':
    main()
