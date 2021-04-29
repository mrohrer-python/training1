def numbers_add(number1, number2):
    result = number1 + number2
    return result

def get_cube(number):
    return number * number * number

def get_square_cube(number):
    square = number * number
    cube = number * number * number
    return square, cube

print(numbers_add(22, 5))
print(numbers_add(100, 333))
print(get_cube(5))
square, cube = get_square_cube(4)
print(square)
print(cube)

