print('Digite 2 números inteiros:')
n1 = int(input('1° número: '))
n2 = int(input('2° número: '))
if n1>n2:
    print('O 1° número ({}) é maior que o 2° número ({})'.format(n1, n2))
elif n2>n1:
    print('O 2° número ({}) é maior que o 1° número ({})'.format(n2, n1))
else:
    print('O 1° número ({}) é igual ao 2° número ({})'. format(n1, n2))
