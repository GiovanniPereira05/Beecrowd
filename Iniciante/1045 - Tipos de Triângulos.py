A,B,C = list(map(float, input().split()))
Lados = [A,B,C]
Lados.sort(reverse=True)

#print(Lados)

if Lados[0] >= Lados[1]+Lados[2]:
    print('NAO FORMA TRIANGULO ')

else:    
    if Lados[0]**2 == Lados[1]**2 + Lados[2]**2:
        print('TRIANGULO RETANGULO')
    
    if Lados[0]**2 > Lados[1]**2 + Lados[2]**2:
        print('TRIANGULO OBTUSANGULO')
    
    if Lados[0]**2 < Lados[1]**2 + Lados[2]**2:
        print('TRIANGULO ACUTANGULO')
    
    if Lados[0] == Lados[1] and Lados[1] == Lados[2]:
        print('TRIANGULO EQUILATERO')
    
    if Lados[0] == Lados[1] != Lados[2] or Lados[1] == Lados[2] != Lados[0]:
        print('TRIANGULO ISOSCELES')
