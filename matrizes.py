print('Vamos multiplicar Matrizes! ')
n = int(input('Digite a dimensão da Matriz A (Linha):'))
m = int(input('Digite a dimensão da Matriz A (Coluna):'))

matriz1 = []
for l in range(n):
    linha = []
    for c in range(m):
        linha.append(int(input(f'Digite o número para linha {l + 1}, coluna {c + 1}: ')))
    matriz1.append(linha)

print('Matriz A: ')


def retorna_matriz1():
    for l in range(n):
        for c in range(m):
            print(f'[{matriz1[l][c]:^5}]', end='')
        print()


retorna_matriz1()

matriz2 = []

x = int(input('Digite a dimensão da Matriz B (Linha):'))
y = int(input('Digite a dimensão da Matriz B (Coluna):'))
for l in range(x):
    linha = []
    for c in range(y):
        linha.append(int(input(f'Digite o numero para linha {l + 1}, coluna {c + 1}: ')))
    matriz2.append(linha)

print('Matriz B: ')


def retorna_matriz2():
    for l in range(x):
        for c in range(y):
            print(f'[{matriz2[l][c]:^5}]', end='')
        print()


retorna_matriz2()

if m == x:
    matriz3 = []
    for i in range(n):
        matriz3.append([])
        for j in range(y):
            mult = 0
            for k in range(m):
                mult = mult + (matriz1[i][k] * matriz2[k][j])
            matriz3[i].append(mult)
    print('--' * 50)
    print('Analisando as matrizes... ')
    print('..' * 50)
    print('Multiplicação possível... ')
    print('..' * 50)
    print("Resultado da multiplicação das duas matrizes:")
    for i in range(n):
        for j in range(y):
            print(f'[{matriz3[i][j]:^5}]', end=" ")
        print()
else:
    print ('--'*50)
    print ('Analisando as matrizes... ')
    print('..' * 50)
    print('Impossível, coluna da 1º matriz é diferente da linha da 2º Matriz!')