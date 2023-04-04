valor_conta = 0
print('\033[1m\033[31mPIZZARIA DIB\U0001F355\033[0m')
print("""Tamanhos de pizza disponíveis:
\033[32m(P)\033[0mPizza Pequena: R$15,00
\033[32m(M)\033[0mPizza Média: R$20,00
\033[32m(G)\033[0mPizza Grande: R$25,00
Observação: digite a \033[32minicial\033[0m do tamanho desejado para continuar.""")
print(' ' * 50)
while True:
    tamanho = str(input('Você deseja qual \033[32mtamanho\033[0m de pizza?: ')).strip().upper()[0]
    if tamanho in ['P', 'M', 'G']:
            break
    else:
        print('\033[31m\u274cErro: digite apenas P, M ou G.\033[0m')
if tamanho == 'P':
    valor_conta = 15
    pizza = 'Pequena'
    print('\033[32mVocê escolheu a Pizza Pequena.\U0001F355\U0001F44D\033[0m')

elif tamanho == 'M':
    valor_conta = 20
    pizza = 'Média'
    print('\033[32mVocê escolheu a Pizza Média.\U0001F355\U0001F44D\033[0m')
elif tamanho == 'G':
    valor_conta = 25
    pizza = 'Grande'
    print('\033[32mVocê escolheu a Pizza Grande.\U0001F355\U0001F44D\033[0m')

print('\033[36m+=\033[0m' * 50)
print("""Valor do Pepperoni para cada pizza:
\033[31mPepperoni\033[0m para \033[32mPizza Pequena\033[0m: R$2,00
\033[31mPepperoni\033[0m para \033[32mPizza Média\033[0m: R$3,00
\033[31mPepperoni\033[0m para \033[32mPizza Grande\033[0m: R$3,00
Observação: Se você quiser pepperoni na sua pizza, o valor será acrescentado automaticamente .
Digite apenas S ou N na resposta.
S = Sim
N = Não""")
while True:
    quer_pepperoni = str(input('Você deseja adicionar pepperoni na sua pizza?[S/N]: ')).strip().upper()[0]
    if quer_pepperoni in ['S', 'N']:
            break
    else:
            print('\033[31m\u274cErro: digite apenas S ou N.\033[0m')
if quer_pepperoni == 'S' and tamanho == 'P':
    valor_conta= valor_conta +2
    tem_pepperoni = '+ Pepperoni'
    print('\033[31mVocê escolheu adicionar Pepperoni.\U0001F44D\033[0m')

elif quer_pepperoni == 'S' and tamanho == 'M':
    valor_conta= valor_conta +3
    tem_pepperoni = '+ Pepperoni'
    print('\033[31mVocê escolheu adicionar Pepperoni\U0001F44D\033[0m')

elif quer_pepperoni == 'S' and tamanho == 'G':
    valor_conta= valor_conta +3
    tem_pepperoni = '+ Pepperoni'
    print('\033[31mVocê escolheu adicionar Pepperoni.\U0001F44D\033[0m')

else:
    valor_conta = valor_conta
    tem_pepperoni = ''
print('\033[36m+=\033[0m' * 50)
print("""Valor de \033[33mqueijo extra\033[0m para qualquer pizza: R$1,00
Observação: Se você quiser queijo extra na sua pizza,o valor será acrescentado automaticamente.
Digite apenas S ou N na resposta.
S = Sim
N = Não""")
while True:
    quer_queijo=str(input('Você deseja adicionar queijo extra na sua pizza?[S/N]: ')).strip().upper()[0]
    if quer_queijo in ['S', 'N']:
        break
    else:
        print('\033[31m\u274cErro: digite apenas S ou N.\033[0m')

if quer_queijo == 'S' and tamanho == 'P':
    valor_conta= valor_conta +1
    tem_queijo = '+ Queijo extra'
    print('\033[33mVocê escolheu adicionar queijo extra.\U0001F9C0\033[0m')
elif quer_queijo == 'S' and tamanho == 'M':
    valor_conta= valor_conta +1
    tem_queijo = '+ Queijo extra'
    print('\033[33mVocê escolheu adicionar queijo extra.\U0001F9C0\033[0m')
elif quer_queijo == 'S' and tamanho == 'G':
    valor_conta= valor_conta +1
    tem_queijo = '+ Queijo extra'
    print('\033[33mVocê escolheu adicionar queijo extra.\U0001F9C0\033[0m')

else:
    valor_conta = valor_conta
    tem_queijo = ''
import time
print('\033[36m+=\033[0m' * 50)
print('\U0001F551 Calculando o total da conta...')
time.sleep(5)
print(f'\033[32m💰 Seu pedido de 1 \033[1mPizza {pizza} {tem_pepperoni} {tem_queijo} ficou no total R$:{valor_conta:.2f}\033[0m')
