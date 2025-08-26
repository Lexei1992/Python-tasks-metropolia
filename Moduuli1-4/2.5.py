luoti = 13.3
naula = 13.3 * 32
leiviskä = 13.3 * 32 * 20

leiviskät = float(input("Anna Leviskät"))
naulat = float(input("Anna naulat"))
luodit = float(input("Anna luodit"))

kokonaispaino = leiviskät * leiviskä + naulat * naula + luodit * luoti
kilot, grammat = divmod(kokonaispaino, 1000)

print(f"Massa nykymittojen mukaan:\n{int(kilot)} kilogrammaa ja {grammat:.2f} grammaa.")