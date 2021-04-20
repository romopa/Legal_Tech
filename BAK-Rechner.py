# Programm 1: BAK-Rechner
# (c) M Rowold 2021-04-18

menge_alkohol_liter = float(input("Wieviele Liter Alkohol wurden getrunken? (in Liter, z.B. 1.5) "))
alkohol_anteil = float(input("Alkoholanteil in Prozent (z.B. 0.12): "))
gewicht_der_person =float(input("Wieviel wiegt die Person? (in kg) "))
masse_alkohol = menge_alkohol_liter *alkohol_anteil*0.8
geschlecht = input("Ist die getestete Person ein Mann oder eine Frau? (M oder F) ")
if geschlecht == "M":
    reduktionsfaktor=float(0.7)
    geschlecht_name = "Mann"
elif geschlecht == "F":
    reduktionsfaktor=float(0.6)
    geschlecht_name = "Frau"
else:
    print("Fehlerhafte Eingabe, bitte starten Sie das Programm erneut")
    quit()  # Beendet laufendes Programm
bak = (masse_alkohol)/(gewicht_der_person*reduktionsfaktor)
bak_round = round(bak, 3)
print("")
print("=================")
print("[Zusammenfassung]")
print("Geschlecht:", geschlecht_name)
print("Gewicht: ", gewicht_der_person, "kg")
print("Getrunkener Alkohol: ", menge_alkohol_liter, "Liter")
print("Alkoholanteil in Prozent: ", alkohol_anteil)
print("=================")
print("")
print("BAK: ", bak_round, "Promille")
