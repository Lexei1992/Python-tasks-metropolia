luvut = []

while True:
    luku = input("Anna luku (tyhjä lopettaa): ")
    if luku == "":
        break
    luku = int(luku)
    print(f"Annoit luvun: {luku}")
    luvut.append(luku)

if luvut:
    luvut.sort(reverse=True)
    suurimmat = luvut[:5]
    print("Viisi suurinta lukua suurimmasta pienimpään:")
    for l in suurimmat:
        print(l)
else:
    print("Et antanut yhtään lukua")



