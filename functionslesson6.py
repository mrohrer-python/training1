#Option1
def say_hello(name):
    print("Hello {0}".format(name))

say_hello(name="Markus")
say_hello(name="Michael")

#Option2
def say_hello(name):
    return "Hello {0}".format(name)

hello_str1 = say_hello(name="Markus")
print(hello_str1)
hello_str2 = say_hello(name="Michael")
print(hello_str2)

#Option3
def say_hello(name):
    return "Hello {0}".format(name)

hello_str1 = say_hello(name="Markus")
print(hello_str1)
print(say_hello(name="Michael"))
