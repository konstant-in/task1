# Модивицировать код, так чтобы задание можно было вводить в строке в формате "операнд1 операция операнд2"
formula = input('Введите вычисляемое выражение в формате "число1 операция число2":')
lst = formula.split()
if len(lst) != 3:
    print("Элементов в выражении должно быть ровно 3!")
    exit(0)
operand1 = float(lst[0])
operand2 = float(lst[2])
oper = lst[1]
if oper == '+':
    z = operand1 + operand2
elif oper == '-':
    z = operand1 - operand2
elif oper == '*':
    z = operand1 * operand2
elif oper == '/':
    z = operand1 / operand2
elif oper == '//':
    z = operand1 // operand2
else:
    print("Тип операции «", oper, "» не распознан!")
    exit(0)
print(operand1, oper, operand2, "=", z)
