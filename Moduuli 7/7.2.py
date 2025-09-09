print("Syötä nimiä! Tyhjän vastauksen antaminen lopettaa nimien keräilyn")

nimet = set()



while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Nimi on jo listassa!")
    else:
        nimet.add(nimi)
        print("Uusi nimi syötetty!")

print(nimet)