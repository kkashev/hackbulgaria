def is_int_palindrom(n):
    a = str(n)
    b = a[::-1]

    if a == b:
        return True


def main():
    print(is_int_palindrom(999))

if __name__ == '__main__':
    main()
