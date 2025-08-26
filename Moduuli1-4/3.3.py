sukupuoli = input("Oletko mies vai nainen? Vastaa M, jos olet mies ja N, jos olet nainen: ")
mies = "M"
nainen = "N"

if sukupuoli == mies or sukupuoli == nainen:
    hemo = float(input("Anna hemoglobiinin määrä: "))

    if sukupuoli == mies:
        if hemo < 134:
            print("Hemoglobiini on alhainen")
        elif hemo > 195:
            print("Hemoglobiini on korkea")
        else:
            print("Hemoglobiini on normaali")
    else:
        if hemo < 117:
            print("Hemoglobiini on alhainen")
        elif hemo > 175:
            print("Hemoglobiini on korkea")
        else:
            print("Hemoglobiini on normaali")
else:
    print("Sukupuoli on määritetty väärin, vastaa M jos olet mies ja N jos olet nainen, muista iso kirjain!")