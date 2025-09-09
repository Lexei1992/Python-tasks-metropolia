print("Syötetään kokonaislukuja listaan!")

def karsi_parittomat(luvut):
    parilliset = []
    for i in luvut:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

luvut = []
koko = int(input("Kuinka monta numeroa haluat syöttää listaan? "))

for i in range(koko):
    luvut.append(int(input("Anna kokonaisluku: ")))

karsittu = karsi_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)
