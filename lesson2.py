# loops / Schleifen
# Beispiel var_a, var_b = 10, 6

secret = 15

# guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
# if guess == secret: # "==" = Vergleich
#    print("Gratuliere - gewonnen. Es ist Nummer 15")
# else:
#    print ("Falsch... Die richtige Zahl war NICHT " + str(guess))

secret = 16
guess = 0
while guess != secret: # "!=" Nicht-gleich
    guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
    if guess == secret:  # "==" = Vergleich
        print("Gratuliere - gewonnen. Es ist Nummer 16.")
    else:
        print("Falsch... Die richtige Zahl war NICHT " + str(guess))
