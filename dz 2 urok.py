from time import perf_counter


class Sneaker:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price


class SneakerStore:
    def __init__(self):
        self.stock = []

    def add_sneaker(self, brand, size, price):
        sneaker = Sneaker(brand, size, price)
        self.stock.append(sneaker)
        print("Добавлены кроссовки:", brand, size, price)

    def display_stock(self, size=None):
        if not self.stock:
            print("Склад пустой")
        else:
            available_sneakers = [s for s in self.stock if s.size == size] if size else self.stock
            if available_sneakers:
                print("Доступные кроссовки:")
                for sneaker in available_sneakers:
                    print(sneaker.brand, sneaker.size, sneaker.price)
            else:
                print("Кроссовок подходящего размера нету")

    def buy_sneaker(self, person, brand, size):
        for sneaker in self.stock:
            if sneaker.brand == brand and sneaker.size == size:
                if person.budget >= sneaker.price:
                    person.budget -= sneaker.price
                    self.stock.remove(sneaker)
                    print("Ты купил " + brand + " " + str(size) + " за " + str(
                        sneaker.price) + ". Остаток бюджета: " + str(person.budget))
                    return
                else:
                    print(person.name + ", у вас недостаточно средств")
                    return
        print(person.name + ", кроссовок " + brand + " размера " + str(size) + " нет в наличии")


class Person:
    def __init__(self, name, budget, size):
        self.name = name
        self.budget = budget
        self.size = size

    def purchase_sneaker(self, store, brand):
        store.buy_sneaker(self, brand, self.size)


# Пример использования
store = SneakerStore()
store.add_sneaker("Nike", 43, 25000)
store.add_sneaker("Adidas", 40, 20000)
store.add_sneaker("Puma", 43, 25000)

person_name = input("Введите ваше имя: ")
budget = int(input("Введите ваш бюджет: "))
size = int(input("Введите ваш размер ноги: "))
person = Person(person_name, budget, size)

# Отображение кроссовок по размеру
print(person_name + "доступные кроссовки вашего размера: ")
store.display_stock(size)

# Выбор кроссовок для покупки
brand = input("Введите марку кросс: ")
person.purchase_sneaker(store, brand)
store.display_stock()
