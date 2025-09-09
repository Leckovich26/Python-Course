import random

random_Number= random.randint(0, 100)

score=0

while True:
    
    score += 1
    guess= input("Adivina el numero : ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Por favor digite un numero")
        continue

    if guess== random_Number:
        print("Numero adivinado.")  
        break  
    elif guess > random_Number:
        print("El numero digitado es mayor.")
    else:
        print("El numero digitado es menor.")

print(f"Lo lograste en {str(score)} intentos.")

        

