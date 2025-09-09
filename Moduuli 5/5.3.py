print("Katsotaan onko luku alkuluku! Tyhjä lopettaa ohjelman")

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = int(luku)

    if luku < 2:
        print("Ei ole alkuluku!")
    else:
        on_alkuluku = True
        for i in range(2, luku):
            if luku % i == 0:
                on_alkuluku = False
                break

        if on_alkuluku:
            print("On alkuluku!")
        else:
            print("Ei ole alkuluku!")