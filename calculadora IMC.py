print('Bem vindo a calculadora de IMC')
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (M): '))
imc = peso / (altura **2)
imc_truncado = imc.__trunc__()
print(f'O imc do índividuo equivale a {imc_truncado}')