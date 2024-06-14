def soma(x,y):
    return x + y

def subtração(x,y):
    return x - y

def multiplicação(x,y):
    return x * y

def divisão(x,y):
    return x / y 

print('Bem-vindo a Calculadora')

while True:
    escolha = input('Digite a opção desejada: 1 - Soma. 2 - Subtração. 3 - Multiplicação. 4 - Divisão. 5 - Encerrar Programa. \n')
    if escolha == '5':
        print('Programa encerrado')
        break

    if escolha == '1':
        try:
            print('Opção escolhida: Soma')
            x = float(input('Digite o primeiro valor: '))
            y = float(input('Digite o segundo valor: '))
            print(f'Resultado: {soma(x,y):.2f}')
        except ValueError:
            print('Valor inválido. Por favor digite um número')
    
    elif escolha == '2':
        try:
            print('Opção escolhida: Subtração')
            x = float(input('Digite o primeiro valor: '))
            y = float(input('Digite o segundo valor: '))
            print(f'Resultado: {subtração(x,y):.2f}')
        except ValueError:
            print('Valor inválido. Por favor digite um número')
            
    elif escolha == '3':
        try:
            print('Opção escolhida: Multiplicação')
            x = float(input('Digite o primeiro valor: '))
            y = float(input('Digite o segundo valor: '))
            print(f'Resultado: {multiplicação(x,y):.2f}')
        except ValueError:
            print('Valor inválido. Por favor digite um número.')
    
    elif escolha == '4':
        try: 
            print('Opção escolhida: Divisão')
            x = float(input('Digite o primeiro valor: '))
            y = float(input('Digite o segundo valor: '))
            print(f'Resultado: {divisão(x, y):.2f}')
        except ValueError:
            print('Valor inválido. Por favor digite um número.')
            
    else:
        print('Caractér inválido. Tente novamente!')
        
    
    
     
    
    
