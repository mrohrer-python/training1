a = 33
b = "Hello"
c = [1, 2, 3]

a = 0
b = a
b += 20
print(a)
print(id(a))
print(id(b))
print(id(a) == id(b))

a = [1, 2, 3]
b = a
b += [55]
print(a)
print(a)
print(id(a) == id(b))