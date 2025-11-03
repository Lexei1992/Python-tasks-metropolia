class Auto:
    def __init__(self, rekNo, topSpeed):
        self.rekNo = rekNo
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.distance = 0


auto1 = Auto("ABC-123", 142)
print(f"Auton rekisterinumero on: {auto1.rekNo}, huippunopeus on: {auto1.topSpeed}km/h, tämänhetkinen nopeus on: {auto1.currentSpeed}km/h, autolla on ajettu {auto1.distance} km.")