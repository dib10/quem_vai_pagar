print('Bem vindo ao tip calculator!')
totalconta = float(input('Qual foi o total da conta?: R$ '))
porcentagem = int(input('Qual a porcentagem de gorjeta que você deseja dar? (10, 12 ou 15): '))
if porcentagem not in [10, 12, 15]:
    print('Porcentagem inválida, calculadora encerrada')
else:
    totalpessoas = int(input('Quantas pessoas para dividir a conta?: '))
    if totalpessoas <= 0:
        print('Número de pessoas inválido, calculadora encerrada')
    else:
        totalcgorjeta = (porcentagem / 100 * totalconta) + totalconta
        total = totalcgorjeta / totalpessoas
        print(f'O total a ser pago por cada pessoa é R${total:.2f}')
