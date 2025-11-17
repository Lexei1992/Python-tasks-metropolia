class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivut):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivut = sivut

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailija: {self.kirjailija} \nSivumäärä: {self.sivut}\n")

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Toimittaja: {self.toimittaja}\n")


julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", "200"))

for j in julkaisut:
    j.tulosta_tiedot()


