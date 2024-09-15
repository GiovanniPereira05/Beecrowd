Valor = int(input())
Ano = 0
Mes = 0
Dia = 0

while (Valor > 0):
    if Valor >= 365:
        Ano+= 1
        Valor-= 365
    if Valor >= 30 and Valor < 365:
        Mes+= 1
        Valor-= 30
    if Valor >= 1 and Valor < 30:
        Dia = Valor
        Valor = 0

print(f'{Ano} ano(s)')
print(f'{Mes} mes(es)')
print(f'{Dia} dia(s)')
