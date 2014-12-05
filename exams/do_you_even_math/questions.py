import random


class Questions():
    def __init__(self):
        pass

    def addition_task(self):
        first_summand = random.randrange(0, 10)
        second_summand = random.randrange(0, 10)
        self.answer = first_summand + second_summand
        print("{} + {} = ?".format(first_summand, second_summand))
        user_answer = input("Answer:")
        self.check_answer(int(user_answer))

    def substraction_task(self):
        minuend = random.randrange(0, 10)
        subtrahend = random.randrange(0, 10)
        self.answer = minuend - subtrahend
        print("{} - {} = ?".format(minuend, subtrahend))
        user_answer = input("Answer:")
        self.check_answer(int(user_answer))

    def multiplication_task(self):
        multiplicand = random.randrange(0, 10)
        multiplier = random.randrange(0, 10)
        self.answer = multiplicand * multiplier
        print("{} * {} = ?".format(multiplicand, multiplier))
        user_answer = input("Answer:")
        self.check_answer(int(user_answer))

    def exponentiation_task(self):
        base = random.randrange(0, 10)
        exponent = random.randrange(0, 10)
        self.answer = base ** exponent
        print("{} ^ {} = ?".format(base, exponent))
        user_answer = input("Answer:")
        self.check_answer(int(user_answer))

    def check_answer(self, answer):
        if (self.answer == answer):
            print("Correct, you earned 1 point")
            self.right_answers += 1
        else:
            print("False")
