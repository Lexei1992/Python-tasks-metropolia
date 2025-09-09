kentät = {"EFHK": "Helsinki Vantaan lentoasema",
          "ESSA": "Arlandan Lentoasema"}

while True:
    print("Hei! Haluatko syöttää uuden lentokentän tiedot, hakea olemassa olevia tietoja vai sulkea ohjelman?")
    vastaus = input("Jos haluat syöttää uudet tiedot vastaa U, jos haluat etsiä olemassa olevia tietoja vastaa E, jos haluat lopettaa ohjelman vastaa L: ").upper()
    if vastaus == "U":
        icao = input("Anna lentokentän ICAO koodi: ").upper()
        nimi = input("Anna lentokentän nimi: ")

        kentät[icao] = nimi

    elif vastaus == "E":
        icao = input("Anna kentän ICAO koodi: ").upper()
        if icao in kentät:
            print(f"Kentän {icao} nimi on {kentät[icao]}")
        else:
            print("Kenttää ei löydy järjestelmästä, ole ystävällinen ja syötä kentän tiedot, jos haluat löytää ne jatkossa.")

    elif vastaus == "L":
        print("Ohjelma sulkeutuu!")
        break

    else:
        print("Vastausta ei tunnistettu, yritä uudelleen.")




