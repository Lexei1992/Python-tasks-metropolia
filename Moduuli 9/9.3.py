class Auto:
    def __init__(self, rekNo, topSpeed):
        self.rekNo = rekNo
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.distance = 0

    def kiihdytys(self, amount):
        self.currentSpeed += amount
        if self.currentSpeed > self.topSpeed:
            print(f"Kaasu on pohjassa, mutta ei auta, tämä romu ei kulje enempää kuin {self.topSpeed}km/h")
            self.currentSpeed = self.topSpeed
        elif self.currentSpeed < 0:
            print(f"Vaikka painat jarrupoljinta täydellä voimalla, auto ei silti lähde taaksepäin")
            self.currentSpeed = 0
        print(f"Auton nopeus tällä hetkellä on: {self.currentSpeed}km/h")

    def kulje(self, time):
        matka = time * self.currentSpeed
        self.distance += matka
        print(f"Ajelit: {time}h nopeudella: {self.currentSpeed}km/h joten matkaa kertyi tällä kertaa: {matka}km nyt tällä autolla on ajettu yhteensä: {self.distance}km")


auto1 = Auto("ABC-123", 142)
print(f"Auton rekisterinumero on: {auto1.rekNo}, huippunopeus on: {auto1.topSpeed}km/h, tämänhetkinen nopeus on: {auto1.currentSpeed}km/h, autolla on ajettu {auto1.distance} km.")
auto1.kiihdytys(30)
auto1.kiihdytys(70)
auto1.kiihdytys(50)
auto1.kiihdytys(-200)
auto1.kiihdytys(50)
auto1.kulje(3)
auto1.kiihdytys(-20)
auto1.kulje(2)
