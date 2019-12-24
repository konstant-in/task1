# Модивицировать код, так чтобы задание можно было вводить в строке в формате "операнд1 операция операнд2"
def input_namber(text_of_question):
    return float(input(text_of_question))


formula = input('Введите вычисляемое выражение в формате "число1 операция число2":')
operand1 = 12 # Распарсить строку formula
operand2 = 4 # Распарсить строку formula
oper = "+" # Распарсить строку formula
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
    print("Тип операции не распознан!")
    exit(0)
print(operand1, oper, operand2, "=", z)
