from connection import Base
from sqlalchemy.orm import Session
from highscores import Highscore
from sqlalchemy import create_engine
import random


class Math_game():
    def __init__(self, engine):
        self.answer = 0
        self.engine = engine
        self.session = Session(bind=engine)
        self.right_answers = 0

    def user_interface(self):
        while True:
            print("Choose an option:\n -Start \n -Highscores")
            user_select = input("-->")
            print(user_select)
            if (user_select == "start"):
                username = input("Enter your name: ")
                #self.add_player(username)
                while True:
                    self.randomizing_tasks()

                break
            elif (user_select == "highscores"):
                break
            else:
                print("Invalid command! Try again")

    def add_player(self, name):
        player = Highscore(playername=name, score=self.right_answers)
        self.session.add(player)
        self.session.commit()

    def randomizing_tasks(self):
        chosen_task = random.randrange(1, 4)
        if (chosen_task == 1):
            self.addition_task()
        if (chosen_task == 2):
            self.substraction_task()
        if (chosen_task == 3):
            self.multiplication_task()
        if (chosen_task == 4):
            self.exponentiation_task()

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
            return False
        else:
            print("False")
            return True

    def show_result(self):
        print("Your score is: {}".format(self.right_answers))


def main():
    engine = create_engine("sqlite:///highscores.db")
    Base.metadata.create_all(engine)
    test = Math_game(engine)
    test.user_interface()
    #test.addition_task()
    #test.multiplication_task()
    #test.substraction_task()
    #test.exponentiation_task()
    #test.add_player("Kris")
    #test.show_result()
    #test.randomizing_tasks()
if __name__ == '__main__':
    main()
