import sys
# Добавить в код v3.1 запись в лог-файл всех вычислений
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
    try:
        z = operand1 / operand2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
elif oper == '//':
    try:
        z = operand1 // operand2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
else:
    print("Тип операции «", oper, "» не распознан!", sep="")

try:
    print(operand1, oper, operand2, "=", z)
except NameError: # operand1, operand2, z не определены
    print("Bye")
    exit(0)


log = open('cal.log', 'a')
print(operand1, oper, operand2, "=", z, file=log)
log.close()
