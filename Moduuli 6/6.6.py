import math

def hintaPerAla(halkaisija_cm, hinta_euro):
    halkaisija_m = halkaisija_cm / 100
    sade_m = halkaisija_m / 2
    pinta_ala_m2 = math.pi * sade_m**2
    return hinta_euro / pinta_ala_m2

hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
pizza1 = hintaPerAla(halkaisija1, hinta1)

hinta2 = float(input("Anna toisen pizzan hinta (€): "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
pizza2 = hintaPerAla(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {pizza1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {pizza2:.2f} €/m²")

if pizza1 < pizza2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif pizza2 < pizza1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")
