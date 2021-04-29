# Beispiel: Eingabe Zahl zw. 1 und 100, immer wenn die Ausgabezahl /3 dividierbar ist "fizz", / "buzz"
# Wenn beides zutrifft /3 und /5 "fizzbuzz"

end_zahl = int(input("Bitte Zahl zw. 1 und 100 eingeben: "))

for number in range(1, end_zahl + 1):
    if number % 3 == 0 and number % 5 == 0: # Modulo Operator "%" = restwert einer division,  True wenn kein rest (0)
        print ("fizzbuzz")
    elif number % 3 == 0:
        print ("fizz")
    elif number % 5 == 0:
        print ("buzz")
    else:
        print (number)


