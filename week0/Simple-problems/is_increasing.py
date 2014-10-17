def is_increasing(a):
    for i in range(len(a)):
        if a[i] < a[i+1]:
            return True
        else:
            return False


def main():
    print(is_increasing([1, 2, 3, 2, 5]))

if __name__ == '__main__':
    main()
