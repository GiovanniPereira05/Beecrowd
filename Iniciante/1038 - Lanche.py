A,B = list(map(int, input().split()))
Preço = 0

if A == 1:
    Preço = 4
if A == 2:
    Preço = 4.5
if A == 3:
    Preço = 5
if A == 4:
    Preço = 2
if A == 5:
    Preço = 1.5

Total = Preço*B
print(f'Total: R$ {Total:.2f}')
