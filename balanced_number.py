def is_number_balanced(n):
    string_n = str(n)
    left_part = 0
    right_part = 0
    if len(string_n) == 1:
        return True
    for x in range(len(string_n)):
        left_part += int(string_n)

    for x in range(len(string_n)/2, len(string_n)):
        right_part += int(string_n)

    return left_part == right_part


def main():
    print(is_number_balanced(121))

if __name__ == '__main__':
    main()
