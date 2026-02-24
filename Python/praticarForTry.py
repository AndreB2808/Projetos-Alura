#1
nubs = [1,2,3,4,5,6,7,8,9,10]
nomes = ['André', 'Cazum8', 'Celso', 'Mateus']
anos = [2005,2024]
#2
bestmine = ["1.13", "1.14", "1.16", "1.18", "1.21"]
print("Top updates do Minecraft:")
for update in bestmine:
    print(update)
#3 ???
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)
#4
for i in range(10, 0, -1):
    print(i)
#5
x = int(input("Solicitando número: "))
print(f"Tabuada do {x} de 1 a 10:") 
for i in range(1, 11):
    resultado = x * i
    print(resultado)
#6
resulti = 0
nubis = [5,10,15,"mãe", 300,4000,9,"pai",3]
for num in nubis:
    try:
        resulti += num
    except:
        print("Valor inválido detectado e descartado!")
print(f"Resultado da soma: {resulti}")
#7
media = 0
divide = 0
medias = [300,500,2,800,2683]
for nums in medias:
    try:
        media += nums
        divide += 1
    except:
        print("Não foram encontrados números na lista!")
print(f"Média dos números da lista:", media / divide)