def list_to_number(ls):
    number = ""
    for a in ls:
        number += str(a)
    return int(number)


def main():
    print(list_to_number([1, 2, 3, 0, 2, 3]))

if __name__ == '__main__':
    main()
