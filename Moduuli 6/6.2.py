import random

tahkot = int(input("Syötä nopan sivujen määrä: "))

def nopanheitto():
    while True:
        noppa = int(random.randint(1, tahkot))
        print(noppa)
        if noppa == tahkot:
            return False

nopanheitto()