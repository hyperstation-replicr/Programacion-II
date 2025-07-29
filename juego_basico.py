#JUEGO BASICO
import random
numero_secreto = random.randint(1, 10)
intentos = 0
max_intentos = 5
print("¡Adivina el numero!!!!!!!!1111!!!!")
while intentos < max_intentos:
    try:
        guess = int(input("Tu numero11!!!: "))
    except ValueError:
        print("Eso número no  boludo!!!!11.")
        continue

    if guess < 1 or guess > 10:
        print("El número debe estar entre 1 y 101111!!!1!!!111!!!11!!")
        continue
    intentos += 1

    if guess == numero_secreto:
        print("¡Sí!!!!111!1!!111!!!! Adivinaste el número.")
        break
    elif guess < numero_secreto:
        print("Muy bajo111!!!1!!1!!!")
    else:
        print("Muy alto111!!!1!!1")
    print(f"tE queDAN!!!!: {max_intentos - intentos}")

else:
    print(f"Perdiste!!!11!!!!!11!1{numero_secreto}.")
