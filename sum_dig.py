def sum_digits(n):
    s = 0
    n = abs(n)
    while n:
        s += int(n) % 10
        n /= int(10)
    return s


def main():
    print (sum_digits(-1120))

if __name__ == '__main__':
