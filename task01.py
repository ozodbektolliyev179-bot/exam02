from task07 import calculate_cart, cart


def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Nolga bo'lish mumkin emas")
        result = num1 / num2
    else:
        print("Error: Noto'g'ri operator")
    return round(result, 2)
print(calculate(10, 5, '+'))  
print(calculate(10, 5, '-'))
print(calculate(10, 5, '*'))
print(calculate(10, 5, '/'))
print =(calculate_cart(cart))
