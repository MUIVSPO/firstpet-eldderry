def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно!")
    return x / y

def exponentiation(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        raise ValueError("Квадратный корень из отрицательного числа невозможен!")

def main():
    operations = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division,
        '^': exponentiation,
        'sqrt': square_root
    }

    history = []

    while True:
        try:
            operation = input("Выберите операцию (+, -, *, /, ^, sqrt): ")
            if operation not in operations:
                raise ValueError("Неизвестная операция!")

            if operation == 'sqrt':
                number = float(input("Введите число: "))
                result = operations[operation](number)
                print(f"Квадратный корень из {number} равен {result:.2f}")
            else:
                first_number = float(input("Введите первое число: "))
                second_number = float(input("Введите второе число: "))
                result = operations[operation](first_number, second_number)
                print(f"Результат операции: {result:.2f}")

            history.append((operation, first_number, second_number, result))

            show_history = input("Хотите посмотреть историю операций? (y/n): ").lower().strip()
            if show_history == 'y':
                for i, op in enumerate(history):
                    if op[0] == 'sqrt':
                        print(f"{i+1}. Квадратный корень из {op[1]} равен {op[3]:.2f}")
                    else:
                        print(f"{i+1}. {op[1]} {op[0]} {op[2]} = {op[3]:.2f}")

            continue_operation = input("Продолжить выполнение операций? (y/n): ").lower().strip()
            if continue_operation == 'n':
                break

        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()