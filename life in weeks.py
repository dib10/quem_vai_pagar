# 1 ano = 365 dias
# 1 ano = 52 semanas
# 1 ano = 12 meses

print('Se você viver até 90 anos, quanto tempo de vida te resta?')
idade = int(input('Qual é a sua idade?: '))

anos_restantes = 90 - idade
meses_restantes = anos_restantes * 12
semanas_restantes = anos_restantes * 52
dias_restantes = anos_restantes * 365

print(f'Faltam {anos_restantes} anos, {semanas_restantes} semanas, {meses_restantes} meses e {dias_restantes} dias até você completar 90')

