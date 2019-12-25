import sys
# Модивицировать код v3.0, так чтобы сообщения об ошибках были понятна простым пользователям (исключить вывод системных соотщений об ошибках типа)
formula = input('Введите вычисляемое выражение в формате "число1 операция число2":')
lst = formula.split()
if len(lst) != 3:
    print("Элементов в выражении должно быть ровно 3!")
    exit(0)
try:
    operand1 = float(lst[0])
except ValueError:
    print("«", lst[0], "» не является числом!", sep="")
    exit(0)
try:
    operand2 = float(lst[2])
except ValueError:
    print("«", lst[2], "» не является числом!", sep="")
    exit(0)
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
    print("Тип операции «", oper, "» не распознан!", sep="")
    exit(0)
print(operand1, oper, operand2, "=", z)
