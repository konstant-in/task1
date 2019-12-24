def input_namber(text_of_question):
    return float(input(text_of_question))


print("Введите номер операции которую вы хотите ваполнить:")
print("1 - сложение, x + y")
print("2 - вычитание, x - y")
print("3 - умножение, x * y")
print("4 - деление, x / y")
print("5 - целочисленное деление, x // y")
oper = input("Операция номер:")
if oper == '1':
    z = input_namber("x = ") + input_namber("y = ")
    text_of_output = "x + y ="
elif oper == '2':
    z = input_namber("x = ") - input_namber("y = ")
    text_of_output = "x - y ="
elif oper == '3':
    z = input_namber("x = ") * input_namber("y = ")
    text_of_output = "x * y ="
elif oper == '4':
    z = input_namber("x = ") / input_namber("y = ")
    text_of_output = "x / y ="
elif oper == '5':
    z = input_namber("x = ") // input_namber("y = ")
    text_of_output = "x // y ="
else:
    print("Вы ввели несуществующую операцию")
    exit(0)
print(text_of_output, z)
