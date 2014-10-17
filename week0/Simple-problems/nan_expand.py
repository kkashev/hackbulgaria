def iterations_of_nan_expand(expanded):
    string = "Not a"
    return expanded.count(string)


def main():
    print(iterations_of_nan_expand("Not a Not a NaN"))

if __name__ == '__main__':
    main()
