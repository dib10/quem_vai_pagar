import random
import time
lista = []
print('Quem vai pagar a conta?💸')
while True:
    nome = input('👤Digite um nome: ').strip()
    if nome:  # verifica se o nome não está vazio
        lista.append(nome)
        resposta = input('Quer continuar? [S/N]: ').strip().upper()
        if resposta == 'N':
            break
        elif resposta != 'S':
            print('❌Digite apenas S ou N como resposta')

print('\n⌛Estamos sorteando quem pagará a conta...\n')
time.sleep(3)
sorteado = random.choice(lista)
print(f'😎💰O sorteado dessa lista foi: {sorteado.title()}\n')
print(f'{sorteado.title()}, todos lembrarão dessa boa ação! 😉')
