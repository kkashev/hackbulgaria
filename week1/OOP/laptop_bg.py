class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return(self.final_price - self.stock_price)


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    def __init__(self, name):
        self.name = __name__
        self.products_count = {}
        self.total_count = 0
        self._total_income = 0

    def load_new_products(self, product, count):
        if product.name in self.products_count:
            self.products_count[product] += count
        else:
            self.products_count[product] = count

    def list_products(self, product_class):
        for product in self.products_count:
            if isinstance(product, product_class):
                print("{} - {}".format(product.name, self.products_count[product]))

    def sell_product(self, product):
        for product in self.products_count:
            if product in self.products_count:
                if self.products_count[product] > 0:
                    self.products_count[product] -= 1
                    self._total_income += product.profit()
                    return True
        return False

    def total_income(self):
        return(self._total_income)


def main():
    store = Store('Laptop.bg')
    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    store.load_new_products(smarthphone, 2)
    print(store.sell_product(smarthphone))  # True
    print(store.sell_product(smarthphone))  # True
    print(store.sell_product(smarthphone))  # False
    print(store.total_income())


if __name__ == '__main__':
    main()
