def prepare_meal(number):
    res = ""
    while True:
        if number % 3 == 0:
            res += "spam "
            number = number // 3
        else:
            break

    if number % 5 == 0:
        if len(res) > 1:
            res += "and "
        res += "eggs"

    print(res)


def main():
    prepare_meal(45)
if __name__ == '__main__':
    main()
