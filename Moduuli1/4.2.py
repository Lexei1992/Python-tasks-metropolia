print("Muunnetaan tuumat senteiksi, jos annat negatiivisen luvun ohjelma pysähtyy.")
luku = float(input("Anna tuumien määrä"))

while luku >= 0:
    print(f"{luku} tuumaa = {luku * 2.54:.2f} senttimetriä.")
    luku = float(input("Anna tuumien määrä."))