import random

class Auto:
    def __init__(self, rekNo, topSpeed):
        self.rekNo = rekNo
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.distance = 0

    def kiihdytys(self, amount):
        self.currentSpeed += amount
        if self.currentSpeed > self.topSpeed:
            self.currentSpeed = self.topSpeed
        elif self.currentSpeed < 0:
            self.currentSpeed = 0

    def kulje(self, time):
        matka = time * self.currentSpeed
        self.distance += matka

class Kilpailu:
    def __init__(self, nimi, pituus, amount):
        self.nimi = nimi
        self.pituus = pituus
        self.amount = amount
        self.autot = [Auto(f"RCE-{_}{random.randint(0,9)}{random.randint(0,9)}", random.randint(150, 200)) for _ in range(amount)]

    def tunti_kuluu(self):
        for car in self.autot:
            car.kiihdytys(random.randint(-10, 15))
            car.kulje(1)

    def tulosta_tilanne(self):
        for car in self.autot:
            print(f"Auto: {car.rekNo} on nyt ajanut {car.distance}km")

    def kilpailu_ohi(self):
        for car in self.autot:
            if car.distance >= self.pituus:
                return True
        return False

kilpailu1 = Kilpailu("Suuri Romuralli", 8000, 10)
for i, auto in enumerate(kilpailu1.autot):
    print(f"Auton {i +1}: rekisterinumero on: {auto.rekNo} sekä huippunopeus on: {auto.topSpeed}km/h")
kierros = 0

while not kilpailu1.kilpailu_ohi():
    kilpailu1.tunti_kuluu()
    kierros += 1
    kilpailu1.kilpailu_ohi()
    if kierros % 10 == 0:
        kilpailu1.tulosta_tilanne()

kilpailu1.autot.sort(key=lambda car: car.distance, reverse=True)

for i, car in enumerate(kilpailu1.autot, start=1):
    car.currentSpeed = 0
    print(f"Auto {car.rekNo} tuli kilpailussa sijalle {i}, "
          f"huippunopeus: {car.topSpeed}km/h, "
          f"tämänhetkinen nopeus: {car.currentSpeed}km/h, "
          f"ajettu matka: {car.distance:.2f}km")