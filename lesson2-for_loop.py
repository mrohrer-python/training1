secret = 16

for x in range (3):
    guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
    if guess == secret:  # "==" = Vergleich
        print("Gratuliere - gewonnen. Es ist Nummer 16.")
        break # break = beendet schleife
    else:
        print("Falsch... Die richtige Zahl war NICHT " + str(guess))