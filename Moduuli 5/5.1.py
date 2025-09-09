import random
nopat = int(input("Anna noppien määrä: "))

summa = 0
for i in range(nopat):
    noppa = random.randint(1, 6)
    print("Heitetty: " + str(noppa))
    summa += noppa
print("Heitit yhteensä: " + str(summa))