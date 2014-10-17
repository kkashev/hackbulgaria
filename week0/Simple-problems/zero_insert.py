def zero_insert(n):
    num = str(n)
    to_insert = False
    result = ""
    for i in range(len(num)-1):
        to_insert = False
        if num[i] == num[i+1]:
            to_insert = True
        elif (int(num[i]) + int(num[i+1])) % 10 == 0:
            to_insert = True

        result += num[i]
        if to_insert:
            result += "0"

    result += num[len(num)-1]
    return result


def main():
    print(zero_insert(116457))
if __name__ == '__main__':
    main()
