def power(x, y=2):
    """Вернуть x^y."""
    if y == 0:
        return 1
    elif y > 0:
        return x * power(x, y - 1)
    else:
        raise ValueError("y должен быть положительным")


try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except ValueError as e:
    print(f'Ошибка "{e}". Проверьте введённые числаа')
except Exception as e:
    print(f'Ошибка "{e}".')


