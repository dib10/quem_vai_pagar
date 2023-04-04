doisnum = str(input('Escreva dois números: '))
checar =len(doisnum)
if checar!=2:
    print('Voce tem que digitar DOIS numeros!!!')
    print('FIM DO PROGRAMA')
else:
    pegar1=doisnum[0]
    pegar2 = doisnum[1]
    soma = int(pegar1) + int(pegar2)
    print(f'A soma entre o conjunto de números "{doisnum}", vale {soma}')

