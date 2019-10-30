try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    znak = input('Введите оператор (+ - / *): ')

    if znak == '+':
        print(a + b)
    elif znak == '-':
        print(a - b)
    elif znak == '/':
        print(a / b)
    elif znak == '*':
        print(a * b)
except ZeroDivisionError:
    print('Ошибка деления на ноль')
except ValueError:
    print('Ошибка преобразования типов')

