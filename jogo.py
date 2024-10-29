# Adivinhe o numero 
import random
dif = input("Selecione a dificuldade do jogo (fácil/normal/dificil): ").lower()
tentativas = 0

if dif == "facil":
    numero_secreto = random.randint(1, 10)
elif dif == "normal":
    numero_secreto = random.randint(1, 25)
elif dif == "dificil":
    numero_secreto = random.randint(1, 50)
else:
    print("Dificuldade inválida! O jogo será encerrado.")
    exit()

while True:
    numero = int(input("Tente adivinhar o número: "))
    tentativas += 1  # Incrementa o contador de tentativas

    if numero == numero_secreto:
        print("Parabéns, você ganhou!!")
        print(f"Tentativas = {tentativas}")
        break
    else:
        print("Errou, tente novamente!")