#1
num = int(input("1- Insira um número: "))
if num % 2 == 0:
    print("O número é par!")
else:
    print("O número é impar!")   
#2    
idade = int(input("2- Passa a idade pra cá: "))
if -1 < idade < 13:
    print("Tu é uma criança pae.")
elif 12 < idade < 19:
    print("Tu é um adolescente pae.")
elif idade > 18:
    print("Tu é um adulto pae.")
else:
    print("Tu é um linígena pae.")
#3
user = input("3- Insira o login: ")
passw = input("Insira a senha: ")
realU = "RRobyly"
realP = "CelsoHospital12"
if user == realU and passw == realP:
    print("Acesso liberado!")
else:
    print("Acesso recusado!")
#4
xis = int(input("4- Coordenada X: "))
yis = int(input("Coordenada Y: "))
if xis > 0 and yis > 0:
    print("WOW! Primeiro Quadrante!")
elif xis < 0 and yis > 0:
    print("WOW! Segundo Quadrante!")
elif xis < 0 and yis < 0:
    print("WOW! Terceiro Quadrante!")
elif xis > 0 and yis < 0:
    print("WOW! Quarto Quadrante!")
else:
    print("WOW! O ponto está localizado no eixo ou origem!")