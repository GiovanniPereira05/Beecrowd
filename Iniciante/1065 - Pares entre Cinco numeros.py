A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
par = 0

if A % 2 == 0:
    par+=1
if B % 2 == 0:
    par+=1
if C % 2 == 0:
    par+=1
if D % 2 == 0:
    par+=1
if E % 2 == 0:
    par+=1

print(f'{par} valores pares')
    
