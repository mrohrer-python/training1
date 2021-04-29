import random

secret = random.randint(1, 30)

while True: # Endlos-Schleife
    guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
    if guess == secret:  # "==" = Vergleich
        print("Gratuliere - gewonnen. Es ist Nummer " + str(secret))
        break
    elif guess > secret:
        print("Falsch, die gesuchte Zahl ist kleiner.")
    elif guess < secret:
        print("Falsch, die gesuchte Zahl ist größer.")
