def sevens_in_a_row(arr, n):
    status = False
    for i in range(len(arr) - n):
        if arr[i] == 7:
            for a in range(i):
                if arr[i] != 7:
                    break
                else:
                    arr[i] == 7
                    status = True
    return status


def main():
    print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))


if __name__ == '__main__':
    main()
