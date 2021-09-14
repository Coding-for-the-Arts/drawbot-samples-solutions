kraftausdruecke = [
    "Mist",
    "Verdammt",
    "Mannmannmann",
    "Herrgottnochmal",
    "Echt jetzt",
    "Zum Teufel"
    ]
berufe = [
    "Baggerführer",
    "Velokurier",
    "Tierärztin",
    "Verkehrspolizist",
    "Schreinerin",
    "Apotheker",
    "Komponist",
    "Physikerin",
    "Buchhändlerin"
    ]
a = choice(kraftausdruecke)
# pick random element in list
# find out its index
# pop it from the list, so it can’t be picked again
b = berufe.pop(berufe.index(choice(berufe)))
c = choice(berufe)
print(a, "Erwin" + ",", "ich bin", b, "und nicht", c + "!")

