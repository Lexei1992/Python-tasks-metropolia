oikea_tunnus = "python"
oikea_salasana = "tunnus"

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
yritykset = 0

while tunnus != oikea_tunnus or salasana != oikea_salasana:
    yritykset += 1
    if yritykset < 5:
        print("Väärä tunnus tai salasana")
        tunnus = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")
    else:
        print("Pääsy Evätty!")
        break
else:
    print("Oikein!")