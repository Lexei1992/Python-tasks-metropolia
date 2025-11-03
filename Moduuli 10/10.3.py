class Hissi:
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.kerros = alinKerros

    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(self.kerros)

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print(self.kerros)

    def siirry_kerrokseen(self, haluttuKerros):
        while haluttuKerros > self.kerros:
            self.kerros_ylös()
            return
        while haluttuKerros < self.kerros:
            self.kerros_alas()
            return

class Talo:
    def __init__(self, alinKerros, ylinKerros, hissienMäärä):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.hissienMäärä = hissienMäärä
        self.hissit = [Hissi(self.alinKerros, self.ylinKerros) for _ in range(hissienMäärä)]

    def aja_hissiä(self, hissiNro, kohdeKerros):
        while self.hissit[hissiNro].kerros != kohdeKerros:
            self.hissit[hissiNro].siirry_kerrokseen(kohdeKerros)

    def palohälytys(self):
        print("Apua talossa on palohälytys")
        for i, hissi in enumerate(self.hissit):
            self.hissit[i].kerros = hissi.alinKerros
            print(f"Hissi {i +1} on kerroksessa {self.hissit[i].kerros}")

talo1 = Talo(int(input("Luodaan talo, mikä on talon alin kerros?")), int(input("Mikä on talin ylin kerros?")), int(input("Kuinka Monta hissiä talossa on?")))
print(f"Talon alin kerros on: {talo1.alinKerros}, ylin kerros on: {talo1.ylinKerros}, talossa on: {talo1.hissienMäärä} hissiä")

hissiInput = 1
while True:
    hissiInput = int(input(f"Ajellaanpa hissillä, millä hissillä haluat mennä? Tässä talossa on {talo1.hissienMäärä} hissiä. Syöttämällä 0 lopetat ohjelman"))
    if hissiInput == 0:
        break
    kerrosInput = int(input(f"Mihin kerrokseen haluat mennä?"))
    talo1.aja_hissiä(hissiInput - 1, kerrosInput)
for i, hissi in enumerate(talo1.hissit):
    print(f"Hissi {i +1}: on kerroksessa {talo1.hissit[i].kerros}")
talo1.palohälytys()