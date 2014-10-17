def sum_of_min_and_max(arr):
    min = max = arr[0]
    for num in arr:
        if num < min:
            min = num
        if num > max:
            max = num

    return min + max


def main():
    print(sum_of_min_and_max([1, 12, 4, 3, 12, 15]))

if __name__ == '__main__':
    main()
