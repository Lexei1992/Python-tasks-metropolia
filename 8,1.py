import mysql.connector

def hae_kentta_koodilla(koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{koodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]}. Lentokentän sijainti: {rivi[1]}")
    return

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='aleksi',
         password='localallu',
         autocommit=True
         )

koodi = input("Anna lentokentän ICAO koodi: ")
hae_kentta_koodilla(koodi)