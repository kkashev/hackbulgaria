class CashDesk():

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for m in money:
            self.money[m] += money[m]

    def total(self):
        total = 0
        for m in self.money:
            total += int(m) * self.money[m]
        return(total)

    def can_withdraw_money(self, change):
        if change >= 100:
            while self.money[100] > 0 and change >= 100:
                change -= 100
                self.money[100] -= 1
        if change >= 50:
            while self.money[50] > 0 and change >= 50:
                change -= 50
                self.money[50] -= 1
        if change >= 20:
            while self.money[20] > 0 and change >= 20:
                change -= 20
                self.money[20] -= 1
        if change >= 10:
            while self.money[10] > 0 and change >= 10:
                change -= 10
                self.money[10] -= 1
        if change >= 5:
            while self.money[5] > 0 and change >= 5:
                change -= 5
                self.money[5] -= 1
        if change >= 2:
            while self.money[2] > 0 and change >= 2:
                change -= 2
                self.money[2] -= 1
        if change >= 1:
            while self.money[1] > 0 and change >= 1:
                change -= 1
                self.money[1] -= 1
        if change == 0:
            return True
        return False


def main():
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1: 2, 50: 3, 20: 1, 100: 20})
    my_cash_desk.total()
    print(my_cash_desk.can_withdraw_money(120))

if __name__ == '__main__':
    main()
