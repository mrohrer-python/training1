import random
import json

secret = random.randint(1, 30)
attempts = 0

with open("lesson4-game-score.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list.sort()
    print("Top scores: " + str(score_list[:6])) #1: exklusive bestes element; :1 bestes Ergebnis; 1:3 = exkl 1, ab 3 nicht mehr
while True: # Endlos-Schleife
    guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
    attempts += 1 # ident mit attempts = attempts +1

    if guess == secret:  # "==" = Vergleich
        score_list.append(attempts)
        with open ("lesson4-game-score.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Gratuliere - gewonnen. Es ist Nummer " + str(secret))
        print("Attempts: " +str(attempts))
        break
    elif guess > secret:
        print("Falsch, die gesuchte Zahl ist kleiner.")
    elif guess < secret:
        print("Falsch, die gesuchte Zahl ist größer.")