A,B = list(map(int, input().split()))
if A >= B:
    print('O JOGO DUROU', 24+B-A, 'HORA(S)')
else:
    print('O JOGO DUROU', B-A, 'HORA(S)')
        
