import random

lista = []
while True:
    nome= str(input('Digite um nome: '))
    lista.append(nome)
    resposta = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if resposta not in 'SN':
        print('Digite apenas S ou N como resposta')
    elif resposta == '':
            print('Digite uma resposta válida')
    elif resposta == 'N':
        break
print(f'O sorteado dessa lista foi {random.choice(lista)}')
