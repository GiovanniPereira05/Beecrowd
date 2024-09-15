N1,N2,N3,N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
Media = float((N1*2+N2*3+N3*4+N4)/10)


if Media >= 5 and Media <= 6.9:
    NotaExame = float(input())
    print(f'Media: {Media:.1f}')
    print("Aluno em exame.")
    print(f'Nota do exame: {NotaExame:.1f}')    
    if (NotaExame+Media)/2 >= 5:
        print("Aluno aprovado.")
    else: print("Aluno reprovado.")
    print("Media final:", (NotaExame+Media)/2)
elif Media >= 7:
    print(f'Media: {Media:.1f}')
    print("Aluno aprovado.")
else:
    print(f'Media: {Media:.1f}')
    print("Aluno reprovado.")
    

