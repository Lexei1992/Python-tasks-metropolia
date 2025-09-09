print("Luodaan lista kokonaislukuja ja lasketaan ne lopuksi yhteen!")

def yhteenlasku(luvut):
    return sum(luvut)

luvut = []
koko = int(input("Kuinka monta numeroa haluat syöttää listaan? "))

for i in range(koko):
    luvut.append(int(input("Anna kokonaisluku: ")))

tulos = yhteenlasku(luvut)
print("Summa on:", tulos)