a, op, b = map(str.strip, input().split())
a, b = map(int, (a, b))
if op == '+':
    print(a + b)
if op == '-':
    print(a - b)
if op == '*':
    print(a * b)
if op == '/':
    if b != 0:
        print(a / b)
    else:
        print('Ошибка деления на ноль')