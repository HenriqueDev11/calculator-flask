while True:

    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')

    resposta = input('O que você deseja fazer? ')
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))

    if resposta == '1':
        soma = a + b
        print(f'O resultado dessa soma é: {soma} ')
    elif resposta == '2':
        subtracao = a - b
        print(f'O resultado dessa subtração é: {subtracao}')
    elif resposta == '3':
        multiplicacao = a * b
        print(f'O resultado dessa multiplicação é: {multiplicacao}')
    elif resposta == '4':
        if b == 0:
            print('Não foi possível dividir por zero!')
        else:
            divisao = a / b
            print(f'O resultado da divisão é: {divisao}')
    break

