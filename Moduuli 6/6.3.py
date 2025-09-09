print("Muunetaan gallonoita litroiksi! Negatiivinen luku lopettaa ohjelman")

def muunnos():
    gallonat = float(0)
    while gallonat >= 0:
        gallonat = float(input("Anna gallonoiden määrä: "))
        if gallonat < 0:
            print("Syötit negatiivisen luvun, ohjelma sulkeutuu!")
            break
        litrat = gallonat * 3.785
        print(f"{gallonat} Gallonaa on noin {litrat:.2f} litraa!")


muunnos()