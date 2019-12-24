x = y = 0


def intut_namber():
    global x, y
    x = float(input("x = "))
    y = float(input("y = "))


print("Введите номер операции которую вы хотите ваполнить:")
print("1 - сложение, x + y")
print("2 - вычитание, x - y")
print("3 - умножение, x * y")
print("4 - деление, x / y")
print("5 - целочисленное деление, x // y")
oper = input("Операция номер:")
if oper == '1':
    intut_namber()
    z = x + y
elif oper == '2':
    intut_namber()
    z = x - y
elif oper == '3':
    intut_namber()
    z = x * y
elif oper == '4':
    intut_namber()
    z = x / y
elif oper == '5':
    intut_namber()
    z = x // y
else:
    print("Вы ввели несуществующую операцию")
    exit(0)
print("Результат:", z)
