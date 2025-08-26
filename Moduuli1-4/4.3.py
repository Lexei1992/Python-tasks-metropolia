luku_str = input("Anna luku: ")

if luku_str != "":
    luku = int(luku_str)
    pienin = luku
    suurin = luku

    while True:
        luku_str = input("Anna luku: ")
        if luku_str == "":
            break
        luku = int(luku_str)
        print("Annoit luvun:", luku)

        if luku < pienin:
            pienin = luku
        elif luku > suurin:
            suurin = luku

    print(f"Pienin luku oli: {pienin} ja suurin luku oli: {suurin}.")
else:
    print("Et antanut yhtään lukua.")
