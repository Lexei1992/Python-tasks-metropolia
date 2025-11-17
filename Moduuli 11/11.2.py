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

class Polttomoottori(Auto):
    def __init__(self, rekNo, topSpeed, fuelCapacity):
        super().__init__(rekNo, topSpeed)
        self.fuelCapacity = fuelCapacity

class Electric(Auto):
    def __init__(self, rekNo, topSpeed, battery):
        super().__init__(rekNo, topSpeed)
        self.battery = battery

auto1 = Electric("ABC-15", 180, "52.5 kWh")
auto2 = Polttomoottori("ACD-123", 165, "32.3 l")

auto1.kiihdytys(180)
auto2.kiihdytys(165)
auto1.kulje(3)
auto2.kulje(3)
print(auto1.distance)
print(auto2.distance)

