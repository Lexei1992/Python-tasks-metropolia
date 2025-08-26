from random import randint

digit1 = randint(0, 9)
digit2 = randint(0, 9)
digit3 = randint(0, 9)

p2d1 = randint(0, 6)
p2d2 = randint(0, 6)
p2d3 = randint(0, 6)
p2d4 = randint(0, 6)

pin1 = str(digit1) + str(digit2) + str(digit3)
pin2 = str(p2d1) + str(p2d2) + str(p2d3) + str(p2d4)

print("Pin 1 = " + pin1)
print("Pin 2 = " + pin2)
