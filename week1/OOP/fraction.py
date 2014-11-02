class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        return("{}/{}".format(self.nominator, self.denominator))

    def __add__(self, other):
        new_denominator = self.nok(self, other)
        new_nominator = (self.nominator*other.denominator + other.nominator*self.denominator)
        return Fraction(new_nominator, new_denominator)

    def __sub__(self, other):
        new_denominator = self.nok(self, other)
        new_nominator = (self.nominator*other.denominator - other.nominator*self.denominator)
        return Fraction(new_nominator, new_denominator)

    def nok(self, first, second):
        return(first.denominator * second.denominator)


def simplify(first, second):
    new_nominator = 0
    new_denominator = 0
    if first % 2 == 0:
        while first % 2 == 0:
            first // 2 = new_nominator
    elif first % 3 == 0:
        while first % 3 == 0:
            first // 3 = new_nominator
    else:
        new_nominator == first

    if second % 2 == 0:
        while second % 2 == 0:
            second // 2 = new_nominator
    elif second % 3 == 0:
        while second % 3 == 0:
            second // 3 = new_nominator
    else:
        new_denominator = second
    print("{}/{}".format(new_nominator, new_denominator))


def main():
    simplify(10, 2)
if __name__ == '__main__':
    main()
