print('Bem vindo(a) a calculadora de IMC')
peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua altura(M): '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Seu imc é {imc:.2f}, logo voce está abaixo do peso normal')
elif 18.5 <= imc <=24.9:
    print(f'Seu imc é {imc:.2f}, logo voce está com peso normal')
elif 25 <= imc <= 29.9:
    print(f'Seu imc é {imc:.2f}, logo voce está com excesso de peso')
elif 30 <= imc <=34.9:
    print(f'Seu imc é {imc:.2f}, logo voce está com obesidade classe 1')
elif 35 <= imc <=39.9:
    print(f'Seu imc é {imc:.2f}, logo voce está com obesidade classe 2')
elif imc >= 40:
    print(f'Seu imc é {imc:.2f}, logo voce está com obesidade classe 3')






