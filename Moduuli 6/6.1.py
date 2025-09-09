import random

def nopanheitto():
    while True:
        noppa = int(random.randint(1, 6))
        print(noppa)
        if noppa == 6:
            return False

nopanheitto()