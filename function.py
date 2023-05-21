# funçoes

# calculo de compra de maçãs

def loja(nome,quantidade):
    print(f'Olá {nome}')
    resultado = float(quantidade) * 2.15
    print(f'Voce comprou {str(quantidade)} maçãs e o total deu R$ {str(resultado)}')

loja(nome = input('Qual seu nome? '),
     quantidade = input('Quantas maças voce comprou? ')
     )