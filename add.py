def add(a, b):
    if a % 2 == 0:
        if a >= b:
            return a
        else:
            if b % 2 == 0:
                return b + abb(a, b - 1)


first = int(input('Введите число - д начало диапазона: '))
second = int(input('Введите число - конец диапазона: '))
print(f'Значение суммы четных чисел от {first} до {second} - {add(first, second)}')
