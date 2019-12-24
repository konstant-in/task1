def input_namber(text_of_question):
    return float(input(text_of_question))


oper = input("Введите символ операции, которую вы хотите ваполнить (+, -, *, /, //):")
if oper == '+':
    z = input_namber("x = ") + input_namber("y = ")
    text_of_output = "x + y ="
elif oper == '-':
    z = input_namber("x = ") - input_namber("y = ")
    text_of_output = "x - y ="
elif oper == '*':
    z = input_namber("x = ") * input_namber("y = ")
    text_of_output = "x * y ="
elif oper == '/':
    z = input_namber("x = ") / input_namber("y = ")
    text_of_output = "x / y ="
elif oper == '//':
    z = input_namber("x = ") // input_namber("y = ")
    text_of_output = "x // y ="
else:
    print("Вы ввели несуществующую операцию")
    exit(0)
print(text_of_output, z)
