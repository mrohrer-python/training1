import random
import json
import datetime

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0

with open("lesson5-game-score-dict.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    #score_list.sort()
    #print("Top scores: " + str(score_list[:6])) #1: exklusive bestes element; :1 bestes Ergebnis; 1:3 = exkl 1, ab 3 nicht mehr

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " Versuche, Datum: " + score_dict["date"])

while True: # Endlos-Schleife
    guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
    attempts += 1 # ident mit attempts = attempts +1

    if guess == secret:  # "==" = Vergleich
       # score_list.append(attempts)
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        with open ("lesson5-game-score-dict.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Gratuliere - gewonnen. Es ist Nummer " + str(secret))
        print("Attempts: " +str(attempts))
        break
    elif guess > secret:
        print("Falsch, die gesuchte Zahl ist kleiner.")
    elif guess < secret:
        print("Falsch, die gesuchte Zahl ist größer.")