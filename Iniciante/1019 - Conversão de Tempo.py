N = int(input())
S = 0
M = 0
H = 0

while (N > 0):
    if N >= 3600:
        H+= 1
        N-= 3600
    if N >= 60 and N < 3600:
        M+= 1
        N-= 60
    if N < 60:
        S = N
        N = 0

print(f'{H}:{M}:{S}')
