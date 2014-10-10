def contains_digit(number, digit):
    number_str = str(number)
    char = str(digit)
    for symbol in number_str:
        if symbol == char:
            return True
    return False


def main():
    print(contains_digit(42, 2))

if __name__ == '__main__':
    main()
