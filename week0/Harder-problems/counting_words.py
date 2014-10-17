def count_words(arr):
    res = {}
    for word in arr:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1

    return res


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
    main()
