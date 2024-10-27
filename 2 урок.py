from time import perf_counter


class Sneaker:
    def __init__(self,brand,size,price):
        self.brand = brand
        self.size = size
        self.price = price

class SneakerStore:
    def __init__(self):
        self.stock = []
    def add_sneaker(self,brand,size,price):
        sneaker = Sneaker(brand,size,price)
        self.stock.append(sneaker)
        print("Были добавлены"+" "+ brand +" "+ str(size) +" "+ str(price))
    def display_stock(self):
        if self.stock == []:
            print("склад пустой")
        else:
            print("В скаладе есть:")
            for sneaker in self.stock:
                print(sneaker.brand,sneaker.size,sneaker.price)
    def buy_sneaker(self,brand,size,budget):
        for sneaker in self.stock:
                if sneaker.brand == brand and sneaker.size == size:
                    if budget >= sneaker.price:
                        self.stock.remove(sneaker)
                        print("Ты купил " + brand +" "+ str(size))
                        return
                    else:
                        print("у вас не хватает денег")
                        return
        print("В наличии таких кросс нету")
budget = int(input())
store = SneakerStore()
store.add_sneaker("Nike" , 43 , 25000)
store.add_sneaker("Adidas" , 40 , 20000)
store.add_sneaker("Puma" , 43 , 25000)
store.buy_sneaker("Nike", 43, budget)
store.display_stock()