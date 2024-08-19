first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:  # если совпадают все три числа - печатаем 2:
    print(2)
elif first == second or first == third or second == third:  # если совпадают два числа из трёх, печатаем 1:
    print(1)
else:  # если не выполняется ни одно из условий, печатаем 0:
    print(0)
