def contains_digits(number, digits):
    string = str(number)
    count = 0
    for x in range(len(digits)):
        if str(digits[x]) in string:
            count += 1
        if count == len(digits):
            return True
            break
    return False


def main():
    contains_digits(402123, [0, 3, 4])

if __name__ == '__main__':
    main()
