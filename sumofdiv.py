def sum_of_divisors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum


def main():
    print(sum_of_divisors(7))

if __name__ == '__main__':
    main()
