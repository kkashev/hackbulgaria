def is_decreasing(a):
    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            return False
    return True


def main():
    print(is_decreasing([5, 4, 5, 2, 1]))

if __name__ == '__main__':
    main()
