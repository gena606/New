import math

while True:
    oper = input('Ведите операцию которую Вы хотите выполнить из списка:'
                 '+, -, *, /, sin, cos, tg (exit для выхода): ')
    if oper == 'exit':
        break
    if oper == 'sin' or oper == 'cos' or oper == 'tg':
        vol = float(input('Введите значение переменной: '))
        if oper == 'sin':
            result = math.sin(vol)
        elif oper == 'cos':
            result = math.cos(vol)
        else:
            result = math.tan(vol)
        print('Результат -', result)
    elif oper == '+' or oper == '-' or oper == '*' or oper == '/':
        vol1 = float(input('Введите значение первой переменной: '))
        vol2 = float(input('Введите значение второй переменной: '))
        if oper == '+':
            result = vol1 + vol2
        elif oper == '-':
            result = vol1 - vol2
        elif oper == '*':
            result = vol1 * vol2
        else:
            result = vol1 / vol2 if vol2 != 0 else 'Делить на нуль нельзя'
        print('Результат -', result)
    else:
        print('Неправильно задан оператор')
