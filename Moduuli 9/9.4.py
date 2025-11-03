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

cars = []

for i in range(10):
    cars.append(Auto(rekNo="ABC-" + str(i + 1), topSpeed=random.randint(100, 200)))

for car in cars:
    print(f"Auton rekisterinumero on: {car.rekNo}, ja sen huippunopeus on: {car.topSpeed}km/h")

def kilpailu():
    kierros = 0
    while True:
        print(f"Kierros {kierros}")
        kierros += 1
        for car in cars:
            car.kiihdytys(random.randint(-10, 15))
            car.kulje(1)
            print(f"Auto: {car.rekNo} on nyt ajanut {car.distance}km")
            if car.distance >= 10000:
                print("Kisa päättyi")
                return

kilpailu()
cars.sort(key=lambda car: car.distance, reverse=True)

for i, car in enumerate(cars, start=1):
    car.currentSpeed = 0
    print(f"Auto {car.rekNo} tuli kilpailussa sijalle {i}, "
          f"huippunopeus: {car.topSpeed}km/h, "
          f"tämänhetkinen nopeus: {car.currentSpeed}km/h, "
          f"ajettu matka: {car.distance:.2f}km")