N = int(input())
Nota100 = 0
Nota50 = 0
Nota20 = 0
Nota10 = 0
Nota5 = 0
Nota2 = 0
Nota1 = 0

print(N)
while (N > 0):
    if N >= 100:
        Nota100+= 1
        N-= 100
    if N >= 50 and N < 100:
        Nota50+= 1
        N-= 50
    if N >= 20 and N < 50:
        Nota20+= 1
        N-= 20
    if N >= 5 and N < 20:
        Nota5+= 1
        N-= 5
    if N >= 2 and N < 5:
        Nota2+= 1
        N-= 2
    if N >= 1 and N < 2:
        Nota1 = N
        N = 0


print(f'{Nota100} nota(s) de R$ 100,00')
print(f'{Nota50} nota(s) de R$ 50,00')
print(f'{Nota20} nota(s) de R$ 20,00')
print(f'{Nota10} nota(s) de R$ 10,00')
print(f'{Nota5} nota(s) de R$ 5,00')
print(f'{Nota2} nota(s) de R$ 2,00')
print(f'{Nota1} nota(s) de R$ 1,00')
        
        
