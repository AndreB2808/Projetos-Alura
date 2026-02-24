#1
pessoa = {'nome':'André', 'idade':'18', 'cidade':'São Paulo'}
print(f'1- {pessoa}')
pessoa['idade'] = 19
pessoa['profissão'] = 'Vagabundo estudante'
del pessoa['cidade']
print(f'2- {pessoa}')
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(f'3- {numeros_quadrados}')
pessoo = {'nome': 'Amando', 'sexo ativo': 'False'}
if 'sexo ativo' in pessoo:
    print("4- A chave 'sexo ativo' existe no dicionário.")
else:
    print("4- A chave 'sexo ativo' não existe no dicionário.")

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(f'5- {contagem_palavras}')



