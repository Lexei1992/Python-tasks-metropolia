from random import randint
oikea_numero = randint(1, 10)
arvaus = int(input("Arvaa kokonaisluku jota ajattelen välillä 1 ja 10: "))


while oikea_numero != arvaus:
    if arvaus < oikea_numero:
        print("Väärin! Luku on liian pieni")
        arvaus = int(input("Arvaa kokonaisluku jota ajattelen välillä 1 ja 10: "))
    elif arvaus > oikea_numero:
        print("Väärin! Luku on liian suuri")
        arvaus = int(input("Arvaa kokonaisluku jota ajattelen välillä 1 ja 10: "))
else:
    print("Oikein!")