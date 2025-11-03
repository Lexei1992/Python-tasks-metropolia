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

hissi1 = Hissi(1, 5)
uInput = 1
print(
    f"Hissi on kerroksessa {hissi1.kerros}. Tämän hissin alin kerros on: {hissi1.alinKerros} ja ylin kerros on: {hissi1.ylinKerros}")

while uInput != 0:
    print(f" Mihin kerrokseen haluat mennä? Syöttämällä 0 lopetat ohjelman")
    uInput = int(input())
    if uInput == 0:
        break
    elif hissi1.alinKerros <= uInput <= hissi1.ylinKerros:
        while hissi1.kerros != uInput:
            hissi1.siirry_kerrokseen(uInput)
