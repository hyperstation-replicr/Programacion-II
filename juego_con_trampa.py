#JUEGO CON TRAMPA
import random
numero_secreto = random.randint(1, 10)
intentos = 0
max_intentos = 5
print("Adivina el numero!!!!!!!!1111!!!")
while intentos < max_intentos:
    guess = int(input("Tu numero11!!!: "))
    
    if guess == -1:
        print("Tramposo111!!!1!122136662#$%&")
        continue 
    intentos += 1
    if guess == numero_secreto:
        print("¡Sí!!!!111!1!!111!!!! Adivinaste el número.")
        break
    elif guess < numero_secreto:
        print("Muy bajo amigo jiujiujiujiujiujiujiujiujiujiujiujiujiu")
    else:
        print("Muy alto burro 555555555555555555555555555555555555")
    print(f"Intentos restantes: {max_intentos - intentos}")

else:
    print(f"Perdiste boludo, el número era {numero_secreto}...!!!1!!!1!!11!1!112#$#%&32356")
