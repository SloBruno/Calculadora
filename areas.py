from cmath import sqrt
import math

cor_vermelha = '\033[0;31m'
cor_amarela = '\033[0;33m'
cor_reset = '\033[m'

print(cor_vermelha + '-=-'* 10 + cor_reset )
print(cor_amarela + '     Calculadora de Área' + cor_reset)
print(cor_vermelha + '-=-'* 10 + cor_reset )

print()

esc1 = int(input('Digite 1 para Triângulo\nDigite 2 para Quadrilátero\n\n' + cor_amarela + 'Escolha:' + cor_reset))


if esc1 == 1:
    print('Digite 1 para Triângulo Qualquer;\nDigite 2 para Triângulo Equilátero;')

if esc1 == 2:
    print("""
Digite 3 para Quadrado;
Digite 4 para Paralelograma;
Digite 5 para Retângulo;
Digite 6 para Losângulo;
""")


else:
    print('Função não disponível')

tipo = int(input(cor_amarela + 'Escolha:' + cor_reset))

if tipo == 1:
    print()
    a = float(input(cor_amarela + 'Aresta da Base:' + cor_reset))
    b = float(input(cor_amarela + 'Altura:' + cor_reset))
    print()
    print(cor_vermelha + 'Resultado:' + cor_reset + '{:.2f}' .format((a * b) / 2))
    print()

if tipo == 2:
    print()
    c = float(input(cor_amarela + 'Aresta do Triângulo:' + cor_reset))
    print()
    print(cor_vermelha + 'Resultado:' + cor_reset + ' {:.2f}'.format((c ** 2) * math.sqrt(3) / 4))
    print()

if tipo == 3:
    print()
    d = float(input(cor_amarela + 'Aresta do Quadrado:' + cor_reset))
    print()
    print(cor_vermelha + 'Resultado:' + cor_reset + '{:.2f}' .format(d ** 2))
    print()
