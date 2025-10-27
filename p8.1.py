def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.
    Параметры:
    - text (str): строка;
    - shift (int): свдиг.
    Результат:
    str: измененная строка."""
    # Набор кириллических букв
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    spec = '.,?! _-+-=;:"*/1234567890'
    text = [s for s in text]
    for i in range(len(text)):
        if text[i].lower() in letters:
            ind_s = letters.index(text[i].lower())
            ind_new = (ind_s + shift) % len(letters)
            if text[i].lower() == text[i]:
                text[i] = letters[ind_new]
            if text[i].lower() != text[i]:
                text[i] = letters[ind_new].upper()
        elif text[i] in spec:
            text[i] = text[i]
        else:
            raise ValueError("Не тот тип ввода")
    return ''.join(text)


try:
    text = input("Введите предложение: ")
    shift = int(input("Введите сдвиг: "))
    encoded = ceasar(text, shift)
    decoded = text
    print("Зашифрованная строка:", encoded)
    print("Расшифрованная строка:", decoded)
except ValueError as e:
    print(f'Ошибка "{e}". Проверьте тип ввода')
except Exception as e:
    print(f'Ошибка "{e}".')

# --------------
# Пример вывода:
#
# Введите предложение: ПрограММиРОВание С++
# Введите сдвиг: 4
# Зашифрованная строка: УфтзфдРРмФТЖдсмй Х++
# Расшифрованная строка: ПрограММиРОВание С++
