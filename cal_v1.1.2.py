def in1():
    return float(input("x = "))


def in2():
    return float(input("x = "))


print("Введите номер операции которую вы хотите ваполнить:")
print("1 - сложение, x + y")
print("2 - вычитание, x - y")
print("3 - умножение, x * y")
print("4 - деление, x / y")
print("5 - целочисленное деление, x // y")
oper = input("Операция номер:")
if oper == '1':
    z = in1() + in2()
elif oper == '2':
    z = in1() - in2()
elif oper == '3':
    z = in1() * in2()
elif oper == '4':
    z = in1() / in2()
elif oper == '5':
    z = in1() // in2()
else:
    print("Вы ввели несуществующую операцию")
    exit(0)
print("Результат:", z)
