pituus = float(input("Anna kuhan pituus senttimetreinä :"))
if pituus < 37:
    print("Kuha on alamittainen! Laske se takaisin veteen. Sallittuun pituuteen on vielä matkaa: " + str(37 - pituus) + " senttimetriä.")
else:
    print("Onneksi olkoon! Kuha täyttää vaadittavat mitat!")