'''
Python
'''
# Primeiro Codigo

# input maneira de inserir algo na variavel

nome = input('Qual o seu nome ? : ')
x = input('Qual o primeiro numero ? : ')
y = input('Qual o segundo numero ? : ')

''' Para juntar string com numeros, o python precisa de converter o num em string para isso use str()
ou int() para converter em int ou float() e etc...
'''

z = int(x) + int(y)
z = str(z)

print('Olá '+ nome)
print('Resultado da soma é de : ' + z)

# formatar texto

resultado = f'Olá {nome} o resultado da soma dos numeros é {z}'
print(resultado)
