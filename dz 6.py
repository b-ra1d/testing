import time
def measure_time(func, *args, **kwargs):
    start_time = time.time()  
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения функции {func.__name__}: {execution_time:.6f} секунд")
    return result 

def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

def test_measure_time():
    result = measure_time(example_function, 1000000)
    assert result == sum(range(1000000)), "Тест не пройден: неверный результат!"
    def no_op():
        return "Hello, world!"
    result = measure_time(no_op)
    assert result == "Hello, world!", "Тест не пройден: неверный результат!"
    def add(a, b):
        return a + b
    result = measure_time(add, 5, 7)
    assert result == 12, "Тест не пройден: неверный результат!"
    print("Все тесты пройдены!")
test_measure_time()
