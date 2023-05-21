'''
# loop de numeros pares de 1 a 25

for num in range(2,26,2):
  print(num)

'''

# crie um retangulo do tamanho que voce decidir

linhas = input('Quantas linhas? ')
colunas = input('Quantas colunas? ')
simbolo = '.'

linhas = int(linhas)
colunas = int(colunas)

for i in range(linhas):
    for j in range(colunas):
        if i == 0 or i == linhas - 1 or j == 0 or j == colunas - 1:
            print(simbolo, end='')
        else:
            print(' ', end='')
    print()   