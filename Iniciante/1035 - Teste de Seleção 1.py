A,B,C,D = list(map(float, input().split()))

if B > C and D > A and C+D > A+B and C == +C and D == +D and A%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
