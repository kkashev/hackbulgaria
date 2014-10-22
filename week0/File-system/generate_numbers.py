import sys
from random import randint


def main():
    filename = sys.argv[1]
    n = int(sys.argv[2])
    file = open(filename, "w")
    for x in range(n):
        content = randint(0, 1000)
        file.write(str(content))
        file.write(" ")
    file.close

if __name__ == '__main__':
    main()
