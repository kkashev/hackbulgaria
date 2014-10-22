import sys


def main():
    filename = sys.argv[1]

    file = open(filename, "r")
    content = file.read()
    numbers = list(content.split(" "))
    numbers.remove(' ')
    s = 0
    for number in numbers:
        s += int(number)
    print(s)
    file.close

if __name__ == '__main__':
    main()
