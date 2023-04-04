#TRUE
#LOVE
contagemtrue = 0
contagemlove = 0
nome1 = str(input('Digite o primeiro nome: ')).strip().upper()
nome2 = str(input('Digite o segundo nome: ')).strip().upper()
for letra in nome1+nome2:
    if letra in 'TRUE':
        contagemtrue+=1
print(f'Correspondente de letra da palavra TRUE: {contagemtrue}')

for letra in nome1+nome2:
    if letra in 'LOVE':
        contagemlove+=1
print(f'Correspondente de letra da palavra LOVE: {contagemlove}')
resultado = str(contagemtrue)+str(contagemlove)
print(resultado)

if int(resultado) > 90:
    print(f'Sua pontuação é {resultado}, vocês combinam como coca e mentos.')
elif 40<=int(resultado)<=50:
    print(f'Sua pontuação é {resultado}, vocês estão bem juntos.')
else:
    print(f'Sua pontuação é: {resultado}')

