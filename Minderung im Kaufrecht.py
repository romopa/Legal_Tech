# Minderung im Kaufrecht
# (C) Moritz Rowold

def GeldBetrag(text:str)->float:                                                # ->float als Typehint, welches Ergebnis ausgespuckt werden soll
    "Validiere Geldbeträge mit Frage text"
                                                                                # gueltig boolean=False
    while True:                                                                   # Alternative "not gueltig"
        wert=input(text)
        try:
            eingabe=float(wert)
            if(eingabe<0): 
                print("Bitte eine positive Zahl eingeben.")
                                                                                    # break <- damit wird die Schleife beendet 
            else:
                if(round(eingabe,2)!=eingabe): 
                    print("Bitte maximal zwei Nachkommastellen eingeben.")                # Eingabe negativ? -> Fehlermeldung
                else:
                    break
                                                                                # gueltig = True
        except:
            print("Bitte geben Sie eine Kommazahl ein")
                                                                                # Rückgabewert -> muss ein Float-Wert sein (= Kommawert)
    return eingabe

# Kaufpreis muss > 0 sein
Kaufpreis:float=-1
while Kaufpreis <= 0:
    Kaufpreis=GeldBetrag("Bitte geben Sie den Kaufpreis ein: ")

# Keine zusätzliche Bedingung
WahrerWert:float=GeldBetrag("Geben Sie den wahren Wert (mit Mangel) ein: ")

# Bedingung: Größer oder gleich wahrer Wert
HypoWert:float=-1
while HypoWert<WahrerWert:
    HypoWert=GeldBetrag("Geben Sie den hypothetischen Wert (ohne Mangel) ein: ")

GeminderterKaufpreis:float=round(Kaufpreis*WahrerWert/HypoWert, 2)

print("Der geminderte Kaufpreis beträgt %.2f * %.2f / %.2f = %.2f" % (Kaufpreis, WahrerWert, HypoWert, GeminderterKaufpreis))
print("Die Minderung beträgt %.2f." % (Kaufpreis-GeminderterKaufpreis))
