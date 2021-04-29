print (20 % 5)
print (20 % 3)

string_one = "Hallo"
string_two = "Lockdown"

print(string_one + " " + string_two) # simple
print("{0} {1}".format(string_one, string_two)) # meist genutzt
# print("{0} Markus, willkommen im {1}".format(string_one, string_two))
print("%s %s" % (string_one, string_two)) # %s = string, %d = decimal; = old school variante
print(f"{string_one} {string_two}")

x = string_one.lower()
print(string_one.lower()) # kleine Buchstaben
