result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError(f"ValueError: {a} is less than {b}")
        if b > 100:
            raise IndexError(f"IndexError: {b} is greater than 100")
        return a / b
    except ValueError as e:
        print(f"ValueError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: Division by zero")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)
