menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito=float(input('Informe qual o valor de depósito: '))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de: R$ {deposito:.2f}\n"
            print(f'\nDepósito de R$ {deposito:.2f} realizado com sucesso!')
        else:
            print("Valor inválido, tente novamente!")
        
        
    elif opcao == "s":
        saque= float(input('Informe o valor do saque: ')) 
        saldo_excedido = saque>saldo
        limite_excedido = saque>limite
        numero_saques_excedidos = numero_saques>=LIMITE_SAQUES
        
        if saldo_excedido:
            print('Saldo insuficiente para saque! \nTente outro valor!')
        
        elif limite_excedido:
            print('Você excedeu o limite! \nLimite máximo de R$ 500,00 por saque.')
        
        elif numero_saques_excedidos:
            print('Número de saques diários excedidos, volte amanhã!')
            
        
        elif saque> 0 and saque<=saldo:
            saldo-=saque
            extrato += f"Saque de: R$ {saque:.2f}\n"
            numero_saques+= 1
            print(f'\nSaque de R$ {saque:.2f} realizado com sucesso!')
            print (f"\n*** Seu saldo atualizado é de: R$ {saldo:.2f} ***\n")
                  
      
    elif opcao == "e":
        print('\n---------- EXTRATO ----------\n')
        print( 'Extrato sem movimentações\n' if not extrato else f'{extrato}\n' )
        print('\n-----------------------------\n')
        print (f"Seu saldo é de: R$ {saldo:.2f}\n")
        print('\n-----------------------------\n')

    elif opcao == "q":
        print("Obrigado usar nosso banco, volte sempre!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")