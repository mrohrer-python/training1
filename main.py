print("Hello World!") # = string
x = 100 # = integer
y = 5
print(x + y)
string_a = "Hallo" # = string
string_name = "Markus"
print(string_a + " " + string_name + "!")

float_decimal = 33.92 # Test von Datentyp float = Kommazahl
float_ten = 10.0
print(float_decimal * float_ten)

# Boolean = für Steuerung
bool_one = True
bool_two = False
nothing = None

user_name = input("Bitte geben Sie ihren Namen ein: ") #user inputs
print("Hallo " + user_name)
first_integer = int(input("Bitte geben sie Zahl 1 ein: ")) #int = def für integer = notwendig für rechnung (programm arbeitet von innen nach außen)
sec_integer = int(input("Bitte geben sie Zahl 2 ein: "))
print(first_integer * sec_integer)

user_day = input("Please enter day: ")
if user_day == "Monday": # "==" = Vergleich ob ident
    print("Good Morning Monday")
elif user_day == "Tuesday":
    print ("Hi Tuesday")
elif user_day == "Wednesday":
    print ("Ahoi Wednesday")
else:
    print ("Hello")
