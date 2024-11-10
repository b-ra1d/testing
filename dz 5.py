class GeneratorIterator:
    def __init__(self, end):
        self.start = 0 
        self.end = end
    def __iter__(self):
        def gen():
            for i in range(self.start, self.end):
                yield i
        return gen()
try:
    end = int(input("Введите конечное число: "))
    if end <= 0:
        print("Ошибка: конечное число должно быть больше 0.")
    else:
        obj = GeneratorIterator(end) 
        for num in obj:
            print(num + 1) 
except ValueError:
    print("Ошибка: введены некорректные данные. Пожалуйста, введите целое число.")
