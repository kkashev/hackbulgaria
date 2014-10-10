def sum_of_min_and_max(arr):
    min = max = arr[0]
    for num in arr:
        if num < min:
            min = num

        elif num > max:
            max = num

    return max + min


def main():
    print sum_of_min_and_max([1, 2, 5, 10, 5])
if __name__ == '__main__':
    main()
