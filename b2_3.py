a = int(input('a = '))
b = int(input('b = '))
op = input('add/sub/mul/div:')
if op == 'add':
    c = a + b
elif op == 'sub':
    c = a - b
elif op == 'mul':
    c = a * b
elif op == 'div':
    c = a / b
else:
     c = 'Error'
print('Answer = ',c)
    